using UnstoppableVault as vault;
using SimpleToken as simpleToken;
using CallbackNoop as receiver;

methods {
    //     // view
    //     function DOMAIN_SEPARATOR() external returns (bytes32) envfree;
    //     function FEE_FACTOR() external returns (uint256) envfree;
    //     function GRACE_PERIOD() external returns (uint64) envfree;
    //     function allowance(address, address) external returns (uint256) envfree;
    function UnstoppableVault.asset() external returns (address) envfree;

    //     function balanceOf(address) external returns (uint256) envfree;
    //     function convertToAssets(uint256 shares) external returns (uint256) envfree;
    function UnstoppableVault.convertToShares(uint256 assets) external returns (uint256) envfree;

    //     function decimals() external returns (uint8) envfree;
    //     function end() external returns (uint64) envfree;
    //     function feeRecipient() external returns (address) envfree;
    //     function flashFee(address _token, uint256 _amount) external returns (uint256);
    //     function maxDeposit(address) external returns (uint256) envfree;
    //     function maxFlashLoan(address _token) external returns (uint256) envfree;
    //     function maxMint(address) external returns (uint256) envfree;
    //     function maxRedeem(address owner) external returns (uint256) envfree;
    //     function maxWithdraw(address owner) external returns (uint256) envfree;
    //     function name() external returns (string) envfree;
    //     function nonces(address) external returns (uint256) envfree;
    //     function owner() external returns (address) envfree;
    //     function paused() external returns (bool) envfree;
    //     function previewDeposit(uint256 assets) external returns (uint256) envfree;
    //     function previewMint(uint256 shares) external returns (uint256) envfree;
    //     function previewRedeem(uint256 shares) external returns (uint256) envfree;
    //     function previewWithdraw(uint256 assets) external returns (uint256) envfree;
    //     function symbol() external returns (string) envfree;
    function UnstoppableVault.totalAssets() external returns (uint256) envfree;

    function UnstoppableVault.totalSupply() external returns (uint256) envfree;

    //     // nonpayable
    //     function approve(address spender, uint256 amount) external returns (bool);
    //     function deposit(uint256 assets, address receiver) external returns (uint256);
    //     function execute(address target, bytes data) external;
    //     function flashLoan(address receiver, address _token, uint256 amount, bytes data) external returns (bool);
    //     function mint(uint256 shares, address receiver) external returns (uint256);
    //     function permit(address owner, address spender, uint256 value, uint256 deadline, uint8 v, bytes32 r, bytes32 s) external;
    //     function redeem(uint256 shares, address receiver, address owner) external returns (uint256);
    //     function setFeeRecipient(address _feeRecipient) external;
    //     function setPause(bool flag) external;
    function _.transfer(address to, uint256 amount) external => DISPATCHER(true);
    function _.transferFrom(address from, address to, uint256 amount) external => DISPATCHER(true);

    //     function transferOwnership(address newOwner) external;
    //     function withdraw(uint256 assets, address receiver, address owner) external returns (uint256);
    function _.onFlashLoan(address, address, uint256, uint256, bytes) external => DISPATCHER(true);
}

// A valid loan must be less than or equal to the maxFlashLoan amount
// The receiver must have enough balance to pay the fee
// Note that this will often revert due to the use of the ReentrancyGuard library
function isValidLoan(env e, address v, address _receiver, address _token, uint256 amount) returns bool {
    uint256 maxLoan = v.maxFlashLoan(e, _token);
    uint256 fee = v.flashFee(e, _token, amount);
    uint256 receiverBalance = _token.balanceOf(e, _receiver);
    bool balancedSharesAndAssets = v.convertToShares(e, v.totalSupply(e)) == v.totalAssets(e);
    return balancedSharesAndAssets && amount > 0 && amount <= maxLoan && receiverBalance >= fee;
}

function safeIsValidLoan(env e, address v, address _receiver, address _token, uint256 amount) returns bool {
    bool result = isValidLoan@withrevert(e, v, _receiver, _token, amount);
    return lastReverted ? false : result;
}

function isOrderedEnvs(env e1, env e2) returns bool {
    return (e1.block.number < e2.block.number && e1.block.timestamp < e2.block.timestamp) || 
           (e1.block.number == e2.block.number && e1.block.timestamp == e2.block.timestamp) || 
           false;
}

rule isValidLoan() {
    env e;
    uint256 amount;
    address asset = currentContract.asset();
    bytes data;

    bool validLoan = safeIsValidLoan(e, currentContract, receiver, asset, amount);
    currentContract.flashLoan@withrevert(e, receiver, asset, amount, data);
    assert(validLoan <=> !lastReverted, "either an invalid loan reverted or a valid loan succeeded");
}

rule someCallCanStopLoans() {
    env e1;
    env e2;
    uint256 amount;
    address asset = currentContract.asset();
    bytes data;

    require(e1.msg.sender != e2.msg.sender, "e and e1 must be different senders");
    require(isOrderedEnvs(e1, e2), "e1 must be before or same as e2");

    // Make all possible calls to the vault, looking for a call that stops future loans
    method f;
    calldataarg args;
    currentContract.f(e1, args);

    bool validLoan = safeIsValidLoan(e2, currentContract, receiver, asset, amount);
    currentContract.flashLoan@withrevert(e2, receiver, asset, amount, data);
    assert(validLoan <=> !lastReverted, "either an invalid loan reverted or a valid loan succeeded");
}
