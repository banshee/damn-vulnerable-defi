using UnstoppableVault as vault;

methods {
    // view
    function DOMAIN_SEPARATOR() external returns (bytes32) envfree;
    function FEE_FACTOR() external returns (uint256) envfree;
    function GRACE_PERIOD() external returns (uint64) envfree;
    function allowance(address, address) external returns (uint256) envfree;
    function asset() external returns (address) envfree;
    function balanceOf(address) external returns (uint256) envfree;
    function convertToAssets(uint256 shares) external returns (uint256) envfree;
    function convertToShares(uint256 assets) external returns (uint256) envfree;
    function decimals() external returns (uint8) envfree;
    function end() external returns (uint64) envfree;
    function feeRecipient() external returns (address) envfree;
    function flashFee(address _token, uint256 _amount) external returns (uint256);
    function maxDeposit(address) external returns (uint256) envfree;
    function maxFlashLoan(address _token) external returns (uint256) envfree;
    function maxMint(address) external returns (uint256) envfree;
    function maxRedeem(address owner) external returns (uint256) envfree;
    function maxWithdraw(address owner) external returns (uint256) envfree;
    function name() external returns (string) envfree;
    function nonces(address) external returns (uint256) envfree;
    function owner() external returns (address) envfree;
    function paused() external returns (bool) envfree;
    function previewDeposit(uint256 assets) external returns (uint256) envfree;
    function previewMint(uint256 shares) external returns (uint256) envfree;
    function previewRedeem(uint256 shares) external returns (uint256) envfree;
    function previewWithdraw(uint256 assets) external returns (uint256) envfree;
    function symbol() external returns (string) envfree;
    function totalAssets() external returns (uint256) envfree;
    function totalSupply() external returns (uint256) envfree;

    // nonpayable
    function approve(address spender, uint256 amount) external returns (bool);
    function deposit(uint256 assets, address receiver) external returns (uint256);
    function execute(address target, bytes data) external;
    function flashLoan(address receiver, address _token, uint256 amount, bytes data) external returns (bool);
    function mint(uint256 shares, address receiver) external returns (uint256);
    function permit(address owner, address spender, uint256 value, uint256 deadline, uint8 v, bytes32 r, bytes32 s) external;
    function redeem(uint256 shares, address receiver, address owner) external returns (uint256);
    function setFeeRecipient(address _feeRecipient) external;
    function setPause(bool flag) external;
    function transfer(address to, uint256 amount) external returns (bool);
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function transferOwnership(address newOwner) external;
    function withdraw(uint256 assets, address receiver, address owner) external returns (uint256);
}

// A valid loan must be less than or equal to the maxFlashLoan amount
// The receiver must have enough balance to pay the fee
// Note that an amount of 0 is considered a valid loan, but likely not useful
function isValidLoan(env e, address v, uint256 amount, address receiver, address token) returns bool {
    uint256 maxLoan = v.maxFlashLoan(e, token);
    uint256 fee = v.flashFee(e, token, amount);
    uint256 receiverBalance = token.balanceOf(e, receiver);
    return amount <= maxLoan && receiverBalance >= fee;
}

rule isValidLoanR() {
    env e;
    address receiver;
    address token;
    uint256 amount;
    bytes data;

    currentContract.flashLoan(e, receiver, token, amount, data);
    assert(isValidLoan(e, currentContract, amount, receiver, token), "loan should be valid");
}