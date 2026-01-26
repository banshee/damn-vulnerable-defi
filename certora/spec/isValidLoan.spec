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

definition TEN_ETH() returns uint256 = 0x8ac7230489e80000;

rule loanThenOperationThenLoanWorks(method f) filtered { f -> !f.isView } {
    storage initialStorage = lastStorage;

    // The address trying to break the flash loan functionality
    address player;

    // Parameters for the flash loan
    env e;
    uint256 amount;
    bytes data;

    // Pull out values used in a few places
    require asset == currentContract.asset();
    address feeRecipient = currentContract.feeRecipient();
    address owner = currentContract.owner();

    // Don't just make sure everyone, not just player, has a limited amount of funds.
    // Remember that the prover will check states where other accounts have given
    // player approvals, so we need to limit their funds too.
    require forall address addr. asset.balanceOf[addr] < TEN_ETH(), "we dont have unlimited funds in this test";

    // Make sure all the addresses used in the test are different
    require notEqualAndNotZero5(player, currentContract, feeRecipient, loanReceiver, owner), "addresses must be different";

    // The scenario we care about is where player is trying to break the flash loan functionality
    // see test/unstoppable/Unstoppable.t.sol
    require e.msg.sender == player, "send messages as player";

    // When flashLoan returns, we know that we're dealing with all possible
    // states where a flash loan can happen.  All the cases that revert
    // will be ignored.
    flashLoan(e, loanReceiver, asset, amount, data);

    // See if there are operations that can disable making loans
    calldataarg args;
    f(e, args) at initialStorage;

    // If the operation reduced the balance of the vault itself so the loan
    // can't be made, that's not interesting
    require currentContract.maxFlashLoan(e, asset) >= amount, "we dont care about operations that reduce the balance of the vault itself";

    // If the operation made it so we can't afford the fee, that's not interesting
    mathint fee = amount / 20 + 1;
    mathint loanReceiverBalance = asset.balanceOf(loanReceiver);
    require loanReceiverBalance > fee, "make sure loanReceiver has a high enough balance to pay any fees";
    // require loanReceiverBalance + amount + fee < 2 ^ 256, "make sure loanReceiver doesn't overflow when we add the amount and fee";

    // Now try to do another flash loan, looking a revert
    flashLoan@withrevert(e, loanReceiver, asset, amount, data);
    bool loan2Reverted = lastReverted;

    assert !loan2Reverted, "if this reverts, we found a way to block loans after operation";
}
