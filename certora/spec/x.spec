import "SimpleTokenDispatch.spec";
import "SoladyReentrancyGuardHelper.spec";
import "env.spec";
import "equality.spec";
import "nativeBalances.spec";
using UnstoppableVault_Harness as vaultWithHarness;
using SimpleToken as st;
using CallbackBase as loanReceiverFunctions;

methods {
    // // view
    // function UnstoppableVault_Harness.DOMAIN_SEPARATOR() external returns (bytes32) envfree;
    function UnstoppableVault_Harness.FEE_FACTOR() external returns (uint256) envfree;
    // function UnstoppableVault_Harness.GRACE_PERIOD() external returns (uint64) envfree;
    function UnstoppableVault_Harness.INITIAL_PLAYER_TOKEN_BALANCE() external returns (uint256) envfree;
    function UnstoppableVault_Harness.TOKENS_IN_VAULT() external returns (uint256) envfree;
    // function UnstoppableVault_Harness.allowance(address, address) external returns (uint256) envfree;
    function UnstoppableVault_Harness.asset() external returns (address) envfree;
    function UnstoppableVault_Harness.balanceOf(address) external returns (uint256) envfree;
    // function UnstoppableVault_Harness.convertToAssets(uint256 shares) external returns (uint256) envfree;
    // function UnstoppableVault_Harness.convertToShares(uint256 assets) external returns (uint256) envfree;
    // function UnstoppableVault_Harness.decimals() external returns (uint8) envfree;
    // function UnstoppableVault_Harness.end() external returns (uint64) envfree;
    function UnstoppableVault_Harness.feeRecipient() external returns (address) envfree;
    // function UnstoppableVault_Harness.flashFee(address _token, uint256 _amount) external returns (uint256) envfree;
    function UnstoppableVault_Harness.getSoladyReentrancyGuardValue() external returns (uint256) envfree;
    function UnstoppableVault_Harness.isLockedBySoladyReentrancyGuard() external returns (bool) envfree;
    function UnstoppableVault_Harness.loanReceiver() external returns (address) envfree;
    // function UnstoppableVault_Harness.maxDeposit(address) external returns (uint256) envfree;
    function UnstoppableVault_Harness.maxFlashLoan(address _token) external returns (uint256) envfree;
    // function UnstoppableVault_Harness.maxMint(address) external returns (uint256) envfree;
    // function UnstoppableVault_Harness.maxRedeem(address owner) external returns (uint256) envfree;
    // function UnstoppableVault_Harness.maxWithdraw(address owner) external returns (uint256) envfree;
    // function UnstoppableVault_Harness.name() external returns (string) envfree;
    // function UnstoppableVault_Harness.nonces(address) external returns (uint256) envfree;
    function UnstoppableVault_Harness.owner() external returns (address) envfree;
    // function UnstoppableVault_Harness.paused() external returns (bool) envfree;
    // function UnstoppableVault_Harness.previewDeposit(uint256 assets) external returns (uint256) envfree;
    // function UnstoppableVault_Harness.previewMint(uint256 shares) external returns (uint256) envfree;
    // function UnstoppableVault_Harness.previewRedeem(uint256 shares) external returns (uint256) envfree;
    // function UnstoppableVault_Harness.previewWithdraw(uint256 assets) external returns (uint256) envfree;
    // function UnstoppableVault_Harness.symbol() external returns (string) envfree;
    function UnstoppableVault_Harness.totalAssets() external returns (uint256) envfree;
    function UnstoppableVault_Harness.totalSupply() external returns (uint256) envfree;

    // // nonpayable
    // function UnstoppableVault_Harness.approve(address spender, uint256 amount) external returns (bool) envfree;
    // function UnstoppableVault_Harness.deposit(uint256 assets, address receiver) external returns (uint256) envfree;
    // function UnstoppableVault_Harness.execute(address target, bytes data) external envfree;
    // function UnstoppableVault_Harness.flashLoan(address receiver, address _token, uint256 amount, bytes data) external returns (bool) envfree;
    // function UnstoppableVault_Harness.mint(uint256 shares, address receiver) external returns (uint256) envfree;
    // function UnstoppableVault_Harness.permit(address owner, address spender, uint256 value, uint256 deadline, uint8 v, bytes32 r, bytes32 s) external envfree;
    // function UnstoppableVault_Harness.redeem(uint256 shares, address receiver, address owner) external returns (uint256) envfree;
    // function UnstoppableVault_Harness.setFeeRecipient(address _feeRecipient) external envfree;
    // function UnstoppableVault_Harness.setPause(bool flag) external envfree;
    // function UnstoppableVault_Harness.transfer(address to, uint256 amount) external returns (bool) envfree;
    // function UnstoppableVault_Harness.transferFrom(address from, address to, uint256 amount) external returns (bool) envfree;
    // function UnstoppableVault_Harness.transferOwnership(address newOwner) external envfree;
    // function UnstoppableVault_Harness.withdraw(uint256 assets, address receiver, address owner) external returns (uint256) envfree;

    // // pure
    function UnstoppableVault_Harness.getSoladyCodesize() external returns (uint256) envfree;

    function _.onFlashLoan(address initiator, address token, uint256 amount, uint256 fee, bytes data) external => DISPATCH(optimistic=true)[_.onFlashLoan(address, address, uint256, uint256, bytes)];

    function _.loanFee() external envfree;
    function CallbackShim.balanceDuringLoan() external returns (uint256) envfree;
    function CallbackShim.functionId() external returns (uint256) envfree;
}

definition MAX_UINT256() returns uint256 = 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff;

function simpleVault() returns (address, address) {
    address player;
    address player2;
    address feeRecipient = currentContract.feeRecipient();
    require (notEqualAndNotZero5(player, player2, feeRecipient, currentContract.loanReceiver(), currentContract.owner()), "addresses must be different");
    require (isZeroNativeBalance5(player, player2, feeRecipient, currentContract.loanReceiver(), currentContract.owner()), "zero balances cleans up UI");

    require (st == currentContract.asset());
    require (st.balanceOf(feeRecipient) == 0);
    require (st.balanceOf(player) == currentContract.INITIAL_PLAYER_TOKEN_BALANCE());
    require (st.balanceOf(player2) == currentContract.INITIAL_PLAYER_TOKEN_BALANCE());
    require (st.balanceOf(currentContract.loanReceiver()) == currentContract.INITIAL_PLAYER_TOKEN_BALANCE());
    require (currentContract.maxFlashLoan(st) == currentContract.TOKENS_IN_VAULT());
    require (currentContract.balanceOf(currentContract.owner()) == currentContract.TOKENS_IN_VAULT());

    return (player, player2);
}

rule x() {
    address player;
    address player2;
    player, player2 = simpleVault();

    address owner = currentContract.owner();
    require (forall address a . a == owner || currentContract.blarg[a] == 0);

    env e;
    assert (currentContract.blarg(e, player2) == 0);
}