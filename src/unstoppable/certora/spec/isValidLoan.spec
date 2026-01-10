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
    function UnstoppableVault_Harness.convertToShares(uint256 assets) external returns (uint256) envfree;
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
    require(notEqualAndNotZero5(player, player2, feeRecipient, currentContract.loanReceiver(), currentContract.owner()), "addresses must be different");
    require(isZeroNativeBalance5(player, player2, feeRecipient, currentContract.loanReceiver(), currentContract.owner()), "zero balances cleans up UI");

    require(st == currentContract.asset());
    require(st.balanceOf(feeRecipient) == 0);
    require(st.balanceOf(player) == currentContract.INITIAL_PLAYER_TOKEN_BALANCE());
    require(st.balanceOf(player2) == currentContract.INITIAL_PLAYER_TOKEN_BALANCE());
    require(st.balanceOf(currentContract.loanReceiver()) == currentContract.INITIAL_PLAYER_TOKEN_BALANCE());
    require(currentContract.maxFlashLoan(st) == currentContract.TOKENS_IN_VAULT());
    require(currentContract.balanceOf(currentContract.owner()) == currentContract.TOKENS_IN_VAULT());

    address notOwner;
    require(notOwner != currentContract.owner());
    require(currentContract.balanceOf(notOwner) == 0);

    return (player, player2);
}

invariant goodBalances()
    convertToShares(totalSupply()) == totalAssets()
    {
        preserved {
            requireInvariant reentracyLockIsUnlocked();
        }
    }

hook Sstore st._balances[KEY address addr] uint256 newValue (uint256 oldValue) {
    assert(false, "boom");
}

function isValidLoan(env e, address v, address _receiver, address _token, uint256 amount) returns bool {
    requireInvariant(reentracyLockIsUnlocked());
    require(vaultWithHarness == v);

    if (amount == 0 || e.msg.value != 0 || vaultWithHarness.asset() != _token) {
        return false;
    }
    mathint maxLoan = vaultWithHarness.maxFlashLoan@withrevert(_token);
    if (lastReverted) {
        return false;
    }
    if (amount > maxLoan) {
        return false;
    }
    mathint fee = vaultWithHarness.flashFeeAdjustedForBug@withrevert(e, _token, amount);
    if (lastReverted) {
        return false;
    }
    mathint receiverBalance = _token.balanceOf(e, _receiver);
    if (receiverBalance < fee) {
        return false;
    }
    if (receiverBalance + amount > MAX_UINT256()) {
        return false;
    }
    if (amount + fee > MAX_UINT256()) {
        return false;
    }
    mathint totalSupply = vaultWithHarness.totalSupply(e);
    mathint nShares = vaultWithHarness.convertToShares@withrevert(e, assert_uint256(totalSupply));
    if (lastReverted) {
        return false;
    }
    bool balancedSharesAndAssets = nShares == vaultWithHarness.totalAssets(e);
    return balancedSharesAndAssets;
}

function balancesInScope(uint256 amount, address loanReceiver) returns (bool) {
    // checking for maxint overflow is out-of-scope, so just make
    // sure nothing comes very close.
    // also the loanReceiver has at least enough to pay two fees
    mathint m = MAX_UINT256() / 16;
    require(st.balanceOf(loanReceiver) < m);
    require(st.balanceOf(currentContract) < m);
    require(st.balanceOf(currentContract.feeRecipient()) < m);
    require(amount > 0 && amount < m);

    return true;
}

rule isValidLoan() {
    simpleVault();

    env e;
    uint256 amount;
    address asset;
    bytes data;

    address loanReceiver = currentContract.loanReceiver();

    require(balancesInScope(amount, loanReceiver));

    bool validLoan = isValidLoan(e, currentContract, loanReceiver, asset, amount);
    bool result = currentContract.flashLoan@withrevert(e, loanReceiver, asset, amount, data);
    bool flashLoanReverted = lastReverted;
    assert(validLoan <=> !flashLoanReverted, "a valid loan never reverts and an invalid loan always reverts");
    assert(!flashLoanReverted => result, "should either revert or return true");
}

rule isValidSubsequentLoan() {
    address player;
    address player2;
    player, player2 = simpleVault();

    env e;
    uint256 amount;
    address asset;
    bytes data;

    require(e.msg.sender == player);

    address loanReceiver = currentContract.loanReceiver();

    currentContract.flashLoan(e, loanReceiver, asset, amount, data);
    require(loanReceiver.functionId(e) != 2);

    // return the fee
    env e1;
    asset.transferFrom(e1, currentContract.feeRecipient(e), loanReceiver, loanReceiver.loanFee(e));

    mathint functionId = loanReceiver.functionId(e);
    bool isInterestingCallbackFunctionId = functionId != 0 && functionId != 2;

    assert(isInterestingCallbackFunctionId => isValidLoan(e, currentContract, loanReceiver, asset, amount));
}

rule isValidSimpleSubsequentLoan() {
    address player;
    address player2;
    player, player2 = simpleVault();

    env e;
    uint256 amount;
    address asset;
    bytes data;

    method f;
    require(!f.isView);

    require(e.msg.sender == player);

    address loanReceiver = currentContract.loanReceiver();

    bool loan1 = currentContract.flashLoan(e, loanReceiver, asset, amount, data);

    // return the fee
    mathint loanFee = loanReceiver.loanFee(e);
    env e1;
    asset.transferFrom(e1, currentContract.feeRecipient(e), loanReceiver, assert_uint256(loanFee));

    // Make sure there is no operation that can disable making loans
    env e2;
    require(e2.msg.sender == player || e2.msg.sender == player2);
    calldataarg args;
    f(e2, args);

    require(st.balanceOf(e2.msg.sender) >= loanFee, "after trying calls in the previous step the balance still needs to be enough to pay the fee");
    bool loan2 = currentContract.flashLoan@withrevert(e, loanReceiver, asset, amount, data);
    bool loan2Reverted = lastReverted;

    assert(!loan2Reverted && loan1 && loan2);
}

rule flashLoanAlwaysLoansCorrectAmount() {
    simpleVault();

    env e;
    uint256 amount;
    address asset;
    bytes data;

    address receiver = currentContract.loanReceiver();

    mathint receiverBalanceBefore = st.balanceOf(receiver);
    currentContract.flashLoan(e, receiver, st, amount, data);
    assert(receiverBalanceBefore + amount == receiver.balanceDuringLoan(e));
}

rule validate_flashFeeAdjustedForBug() {
    env e;
    uint256 amount;
    address asset;
    bytes data;

    address loanReceiver = currentContract.loanReceiver();

    require(balancesInScope(amount, loanReceiver));

    uint256 expectedFee = vaultWithHarness.flashFeeAdjustedForBug@withrevert(e, asset, amount);
    bool flashFeeAdjustedForBugReverted = lastReverted;
    currentContract.flashLoan(e, loanReceiver, asset, amount, data);
    assert(!flashFeeAdjustedForBugReverted, "if the loan worked flashFeeAdjustedForBug must also work");
    assert(expectedFee == loanReceiver.loanFee(e), "fees must match");
}

rule isValidLoanNeverReverts() {
    env e;
    uint256 amount;
    address asset;
    bytes data;

    address loanReceiver = currentContract.loanReceiver();

    isValidLoan@withrevert(e, currentContract, loanReceiver, asset, amount);
    assert(!lastReverted, "isValidLoan never reverts");
}
