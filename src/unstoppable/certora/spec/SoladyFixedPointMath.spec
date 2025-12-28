import "SimpleTokenDispatch.spec";
import "SoladyReentrancyGuardHelper.spec";
using CallbackNoop as loanReceiver;
using UnstoppableVault_Harness as vaultWithHarness;

methods {
    // // view
    // function UnstoppableVault_Harness.DOMAIN_SEPARATOR() external returns (bytes32) envfree;
    // function UnstoppableVault_Harness.FEE_FACTOR() external returns (uint256) envfree;
    // function UnstoppableVault_Harness.GRACE_PERIOD() external returns (uint64) envfree;
    // function UnstoppableVault_Harness.allowance(address, address) external returns (uint256) envfree;
    function UnstoppableVault_Harness.asset() external returns (address) envfree;
    // function UnstoppableVault_Harness.balanceOf(address) external returns (uint256) envfree;
    // function UnstoppableVault_Harness.convertToAssets(uint256 shares) external returns (uint256) envfree;
    // function UnstoppableVault_Harness.convertToShares(uint256 assets) external returns (uint256) envfree;
    // function UnstoppableVault_Harness.decimals() external returns (uint8) envfree;
    // function UnstoppableVault_Harness.end() external returns (uint64) envfree;
    // function UnstoppableVault_Harness.feeRecipient() external returns (address) envfree;
    // function UnstoppableVault_Harness.flashFee(address _token, uint256 _amount) external returns (uint256) envfree;
    function UnstoppableVault_Harness.getSoladyReentrancyGuardValue() external returns (uint256) envfree;
    function UnstoppableVault_Harness.isLockedBySoladyReentrancyGuard() external returns (bool) envfree;
    // function UnstoppableVault_Harness.maxDeposit(address) external returns (uint256) envfree;
    // function UnstoppableVault_Harness.maxFlashLoan(address _token) external returns (uint256) envfree;
    // function UnstoppableVault_Harness.maxMint(address) external returns (uint256) envfree;
    // function UnstoppableVault_Harness.maxRedeem(address owner) external returns (uint256) envfree;
    // function UnstoppableVault_Harness.maxWithdraw(address owner) external returns (uint256) envfree;
    // function UnstoppableVault_Harness.name() external returns (string) envfree;
    // function UnstoppableVault_Harness.nonces(address) external returns (uint256) envfree;
    // function UnstoppableVault_Harness.owner() external returns (address) envfree;
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

    function _.onFlashLoan(address initiator, address token, uint256 amount, uint256 fee, bytes data) external => DISPATCH(optimistic=true)[CallbackNoop.onFlashLoan(address, address, uint256, uint256, bytes)];
}

use invariant reentracyLockIsUnlocked;
definition MAX_UINT256() returns uint256 = 0xffffffffffffffffffffffffffffffff;

function mulOverflows(uint256 a, uint256 b) returns bool {
    
};

// A valid loan must be less than or equal to the maxFlashLoan amount
// The receiver must have enough balance to pay the fee
// Note that this will often revert due to the use of the ReentrancyGuard library
function isValidLoan(env e, address v, address _receiver, address _token, uint256 amount) returns bool {
    requireInvariant(reentracyLockIsUnlocked);
    require (vaultWithHarness == v);
    mathint ta = vaultWithHarness.totalAssets();
    mathint ts = vaultWithHarness.totalSupply();
    mathint productOfSupplyAndAssets = ta * ts;
    if (productOfSupplyAndAssets > MAX_UINT256()) {
        return false;
    }
    if (amount == 0 || e.msg.sender == 0 || e.msg.value  != 0 || vaultWithHarness.asset() != _token) {
        return false;
    }
    uint256 maxLoan = vaultWithHarness.maxFlashLoan@withrevert(e, _token);
    if (lastReverted) {
        return false;
    }
    if (amount > maxLoan) {
        return false;
    } 
    uint256 fee = vaultWithHarness.flashFee@withrevert(e, _token, amount);
    if (lastReverted) {
        return false;
    }
    uint256 receiverBalance = _token.balanceOf(e, _receiver);
    if (receiverBalance < fee) {
        return false;
    }
    // This will revert if the numbers are too large; 2^256 - 18 for supply, for example
    bool balancedSharesAndAssets = vaultWithHarness.convertToShares@withrevert(e, vaultWithHarness.totalSupply(e)) == vaultWithHarness.totalAssets(e);
    if (lastReverted) {
        return false;
    }
    return balancedSharesAndAssets;
}

function safeIsValidLoan(env e, address v, address _receiver, address _token, uint256 amount) returns bool {
    bool result = isValidLoan@withrevert(e, v, _receiver, _token, amount);
    return lastReverted ? false : result;
}

rule isValidLoan() {
    env e;
    uint256 amount;
    address asset = currentContract.asset();
    bytes data;
    
    require(amount > 0 && e.msg.sender != 0 && e.msg.value  == 0);
    bool validLoan = safeIsValidLoan(e, currentContract, loanReceiver, asset, amount);
    currentContract.flashLoan@withrevert(e, loanReceiver, asset, amount, data);
    assert(validLoan => !lastReverted, "a valid loan never reverts");
    assert(!validLoan => lastReverted, "an invalid loan always reverts");
}

rule isValidLoanNeverReverts() {
    env e;
    uint256 amount;
    address asset = currentContract.asset();
    bytes data;

    bool validLoan = isValidLoan@withrevert(e, currentContract, loanReceiver, asset, amount);
    assert(!lastReverted, "isValidLoan should never revert");
}

// rule someCallCanStopLoans() {
//     env e1;
//     env e2;
//     uint256 amount;
//     address asset = currentContract.asset();
//     bytes data;

//     require(e1.msg.sender != e2.msg.sender, "e and e1 must be different senders");
//     require(isOrderedEnvs(e1, e2), "e1 must be before or same as e2");

//     // Make all possible calls to the vault, looking for a call that stops future loans
//     method f;
//     calldataarg args;
//     currentContract.f(e1, args);

//     bool validLoan = safeIsValidLoan(e2, currentContract, receiver, asset, amount);
//     currentContract.flashLoan@withrevert(e2, receiver, asset, amount, data);
//     assert(validLoan <=> !lastReverted, "either an invalid loan reverted or a valid loan succeeded");
// }
