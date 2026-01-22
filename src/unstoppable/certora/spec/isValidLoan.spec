// SPDX-License-Identifier: Apache-2.0

import "equality.spec";
import "Constants.spec";

using DamnValuableToken as asset;
using SimpleFlashReceiver as loanReceiver;

methods {
    // // // view
    // // function UnstoppableVault_Harness.DOMAIN_SEPARATOR() external returns (bytes32) envfree;
    // function UnstoppableVault_Harness.FEE_FACTOR() external returns (uint256) envfree;
    // // function UnstoppableVault_Harness.GRACE_PERIOD() external returns (uint64) envfree;
    // function UnstoppableVault_Harness.INITIAL_PLAYER_TOKEN_BALANCE() external returns (uint256) envfree;
    // function UnstoppableVault_Harness.TOKENS_IN_VAULT() external returns (uint256) envfree;
    // // function UnstoppableVault_Harness.allowance(address, address) external returns (uint256) envfree;
    // function UnstoppableVault_Harness.asset() external returns (address) envfree;
    // function UnstoppableVault_Harness.balanceOf(address) external returns (uint256) envfree;
    // // function UnstoppableVault_Harness.convertToAssets(uint256 shares) external returns (uint256) envfree;
    // function UnstoppableVault_Harness.convertToShares(uint256 assets) external returns (uint256) envfree;
    // // function UnstoppableVault_Harness.decimals() external returns (uint8) envfree;
    // // function UnstoppableVault_Harness.end() external returns (uint64) envfree;
    // function UnstoppableVault_Harness.feeRecipient() external returns (address) envfree;
    // // function UnstoppableVault_Harness.flashFee(address _token, uint256 _amount) external returns (uint256) envfree;
    // function UnstoppableVault_Harness.getSoladyReentrancyGuardValue() external returns (uint256) envfree;
    // function UnstoppableVault_Harness.isLockedBySoladyReentrancyGuard() external returns (bool) envfree;
    // function UnstoppableVault_Harness.loanReceiver() external returns (address) envfree;
    // // function UnstoppableVault_Harness.maxDeposit(address) external returns (uint256) envfree;
    // function UnstoppableVault_Harness.maxFlashLoan(address _token) external returns (uint256) envfree;
    // // function UnstoppableVault_Harness.maxMint(address) external returns (uint256) envfree;
    // // function UnstoppableVault_Harness.maxRedeem(address owner) external returns (uint256) envfree;
    // // function UnstoppableVault_Harness.maxWithdraw(address owner) external returns (uint256) envfree;
    // // function UnstoppableVault_Harness.name() external returns (string) envfree;
    // // function UnstoppableVault_Harness.nonces(address) external returns (uint256) envfree;
    // function UnstoppableVault_Harness.owner() external returns (address) envfree;
    // // function UnstoppableVault_Harness.paused() external returns (bool) envfree;
    // // function UnstoppableVault_Harness.previewDeposit(uint256 assets) external returns (uint256) envfree;
    // // function UnstoppableVault_Harness.previewMint(uint256 shares) external returns (uint256) envfree;
    // // function UnstoppableVault_Harness.previewRedeem(uint256 shares) external returns (uint256) envfree;
    // // function UnstoppableVault_Harness.previewWithdraw(uint256 assets) external returns (uint256) envfree;
    // // function UnstoppableVault_Harness.symbol() external returns (string) envfree;
    // function UnstoppableVault_Harness.totalAssets() external returns (uint256) envfree;
    // function UnstoppableVault_Harness.totalSupply() external returns (uint256) envfree;

    // // // nonpayable
    // // function UnstoppableVault_Harness.approve(address spender, uint256 amount) external returns (bool) envfree;
    // // function UnstoppableVault_Harness.deposit(uint256 assets, address receiver) external returns (uint256) envfree;
    // // function UnstoppableVault_Harness.execute(address target, bytes data) external envfree;
    // // function UnstoppableVault_Harness.flashLoan(address receiver, address _token, uint256 amount, bytes data) external returns (bool) envfree;
    // // function UnstoppableVault_Harness.mint(uint256 shares, address receiver) external returns (uint256) envfree;
    // // function UnstoppableVault_Harness.permit(address owner, address spender, uint256 value, uint256 deadline, uint8 v, bytes32 r, bytes32 s) external envfree;
    // // function UnstoppableVault_Harness.redeem(uint256 shares, address receiver, address owner) external returns (uint256) envfree;
    // // function UnstoppableVault_Harness.setFeeRecipient(address _feeRecipient) external envfree;
    // // function UnstoppableVault_Harness.setPause(bool flag) external envfree;
    // // function UnstoppableVault_Harness.transfer(address to, uint256 amount) external returns (bool) envfree;
    // // function UnstoppableVault_Harness.transferFrom(address from, address to, uint256 amount) external returns (bool) envfree;
    // // function UnstoppableVault_Harness.transferOwnership(address newOwner) external envfree;
    // // function UnstoppableVault_Harness.withdraw(uint256 assets, address receiver, address owner) external returns (uint256) envfree;

    // // // pure
    // function UnstoppableVault_Harness.getSoladyCodesize() external returns (uint256) envfree;

    // function _.onFlashLoan(address initiator, address token, uint256 amount, uint256 fee, bytes data) external => DISPATCH(optimistic=true)[_.onFlashLoan(address, address, uint256, uint256, bytes)];

    // function _.loanFee() external envfree;
    // function CallbackShim.balanceDuringLoan() external returns (uint256) envfree;
    // function CallbackShim.functionId() external returns (uint256) envfree;
    function asset() external returns (address) envfree;
    function feeRecipient() external returns (address) envfree;
    function owner() external returns (address) envfree;
    function totalAssets() external returns (uint256) envfree;
    function DamnValuableToken.balanceOf(address) external returns (uint256) envfree;
}

function eqExceptSender(env e1, env e2) returns (bool) {
    return e1.msg.value == e2.msg.value && e1.tx.origin == e2.tx.origin && e1.block.timestamp == e2.block.timestamp && e1.block.number == e2.block.number && e1.block.difficulty == e2.block.difficulty && e1.block.gaslimit == e2.block.gaslimit && e1.block.coinbase == e2.block.coinbase && e1.block.basefee == e2.block.basefee && e1.block.blobbasefee == e2.block.blobbasefee;
}

function envWithSender(env e, address newSender) returns env {
    env newE;
    
    // 1. Constrain the sender to be the new address
    require newE.msg.sender == newSender;

    // 2. Constrain all other fields to match the original environment 'e'
    require newE.msg.value == e.msg.value;
    require newE.tx.origin == e.tx.origin;
    require newE.block.timestamp == e.block.timestamp;
    require newE.block.number == e.block.number;
    require newE.block.difficulty == e.block.difficulty;
    require newE.block.gaslimit == e.block.gaslimit;
    require newE.block.coinbase == e.block.coinbase;
    require newE.block.basefee == e.block.basefee;
    require newE.block.blobbasefee == e.block.blobbasefee;

    return newE;
}

hook CODESIZE() uint v {
    require v != assert_uint256(currentContract);
}

rule loanThenOperationThenLoanWorks(method f, method g) filtered { f -> !f.isView, g -> !g.isView } {
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

    // See if are operations that can disable making loans
    calldataarg args;
    f(e, args) at initialStorage;

    require currentContract.maxFlashLoan(e, asset) >= amount, "after operation, flash loan should still be possible";
    // require asset.balanceOf(loanReceiver) < MAX_UINT256() * 5 / 100, "loan receiver should not overflow";

    flashLoan@withrevert(e, loanReceiver, asset, amount, data);
    bool loan2Reverted = lastReverted;

    assert !loan2Reverted, "if this reverts, makeArbitraryCall found a problem";
}
