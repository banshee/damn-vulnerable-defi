// SPDX-License-Identifier: Apache-2.0

import "equality.spec";

using DamnValuableToken as asset;
using UnstoppableVault as vault;
using SimpleFlashReceiver as loanReceiver;

methods {
    function asset() external returns (address) envfree;
    function balanceOf(address account) external returns (uint256) envfree;
    function convertToShares(uint256 assets) external returns (uint256) envfree;
    function feeRecipient() external returns (address) envfree;
    function owner() external returns (address) envfree;
    function totalAssets() external returns (uint256) envfree;
    function totalSupply() external returns (uint256) envfree;
    function asset.balanceOf(address account) external returns (uint256) envfree;
}

function sharesAndAssetsBalance() returns (bool) {
    return convertToShares(currentContract.totalSupply()) == currentContract.totalAssets();
}

invariant sharesAndAssetsBalanceInvariant()
    sharesAndAssetsBalance()
    {
        preserved with (env e) {
            require e.msg.sender != vault, "ignore messages from the vault itself";
            require vault.feeRecipient() != vault, "there should be a guard to prevent this in the contract";
        }
    }

rule loanThenOperationThenLoanWorks(method f) filtered { f -> !f.isView } {
    storage initialStorage = lastStorage;

    address player;

    env e;
    uint256 amount;
    bytes data;

    require asset == currentContract.asset();
    address feeRecipient = currentContract.feeRecipient();
    address owner = currentContract.owner();

    require notEqualAndNotZero5(player, currentContract, feeRecipient, loanReceiver, owner), "addresses must be different";

    require e.msg.sender == player, "send messages as player";

    flashLoan(e, loanReceiver, asset, amount, data);

    // See if there are operations that can disable making loans
    calldataarg args;
    f(e, args) at initialStorage;

    require sharesAndAssetsBalance(), "we already know this breaks the system, so ignore it here";

    // we could add requires that check that player has no approvals from other accounts,
    // but that may mask other problems.  Just make sure that the pool still has enough balance
    // to do the loan.
    require currentContract.maxFlashLoan(e, asset) >= amount, "we dont care about operations that reduce the balance of the vault itself";

    mathint fee = amount / 20 + 1;
    mathint loanReceiverBalance = asset.balanceOf(loanReceiver);
    require loanReceiverBalance > fee, "make sure loanReceiver has a high enough balance to pay any fees";
    require loanReceiverBalance + amount + fee < 2 ^ 256, "make sure loanReceiver doesn't overflow when we add the amount and fee";

    flashLoan@withrevert(e, loanReceiver, asset, amount, data);
    bool loan2Reverted = lastReverted;

    assert !loan2Reverted, "if this reverts, we found a way to block loans after operation";
}
