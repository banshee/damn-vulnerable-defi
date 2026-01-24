// SPDX-License-Identifier: Apache-2.0

import "equality.spec";
import "Constants.spec";
import "isValidLoanErcInvariants.spec";

using SimpleFlashReceiver as loanReceiver;

methods {
    function asset() external returns (address) envfree;
    function convertToShares(uint256 assets) external returns (uint256) envfree;
    function feeRecipient() external returns (address) envfree;
    function owner() external returns (address) envfree;
    function totalAssets() external returns (uint256) envfree;
    function totalSupply() external returns (uint256) envfree;
}

// this is for the Solady reentrancy guard check.  Just make sure codesize is never equal to the contract address.
hook CODESIZE() uint v {
    require v != assert_uint256(currentContract);
}

function sharesAndAssetsBalance() returns (bool) {
    return convertToShares(currentContract.totalSupply()) == currentContract.totalAssets();
}

invariant sharesAndAssetsBalanceInvariant()
    sharesAndAssetsBalance();

rule loanThenOperationThenLoanWorks(method f)
filtered {
    f -> !f.isView
} {
    requireAllErc20Invariants();

    storage initialStorage = lastStorage;

    address player;

    env e;
    uint256 amount;
    bytes data;

    require asset == currentContract.asset();
    address feeRecipient = currentContract.feeRecipient();
    address owner = currentContract.owner();

    require notEqualAndNotZero5(player, currentContract, feeRecipient, loanReceiver, owner), "addresses must be different";

    require e.msg.sender == player;

    flashLoan(e, loanReceiver, asset, amount, data);

    // See if there are operations that can disable making loans
    calldataarg args;
    f(e, args) at initialStorage;

    require sharesAndAssetsBalance(), "we already know this breaks the system, so ignore it here";

    // we could add requires that check that player has no approvals from other accounts,
    // but that may mask other problems.  Just make sure that the pool still has enough balance
    // to do the loan.
    require currentContract.maxFlashLoan(e, asset) >= amount, "we dont care about operations that reduce the balance of the vault itself";

    flashLoan@withrevert(e, loanReceiver, asset, amount, data);
    bool loan2Reverted = lastReverted;

    assert !loan2Reverted, "if this reverts, we found a way to block loans after operation";
}
