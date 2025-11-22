using CallbackShim as callbackReceiver;

methods {
    // view
    function DOMAIN_SEPARATOR() external returns (bytes32) envfree;
    function FEE_FACTOR() external returns (uint256) envfree;
    function GRACE_PERIOD() external returns (uint64) envfree;
    function allowance(address , address ) external returns (uint256) envfree;
    function asset() external returns (address) envfree;
    function balanceOf(address ) external returns (uint256) envfree;
    function convertToAssets(uint256 shares) external returns (uint256) envfree;
    function convertToShares(uint256 assets) external returns (uint256) envfree;
    function decimals() external returns (uint8) envfree;
    function end() external returns (uint64) envfree;
    function feeRecipient() external returns (address) envfree;
    function flashFee(address _token, uint256 _amount) external returns (uint256) ;
    function maxDeposit(address ) external returns (uint256) envfree;
    function maxFlashLoan(address _token) external returns (uint256) envfree;
    function maxMint(address ) external returns (uint256) envfree;
    function maxRedeem(address owner) external returns (uint256) envfree;
    function maxWithdraw(address owner) external returns (uint256) envfree;
    function name() external returns (string) envfree;
    function nonces(address ) external returns (uint256) envfree;
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
    function execute(address target, bytes data) external ;
    function flashLoan(address receiver, address _token, uint256 amount, bytes data) external returns (bool);
    function mint(uint256 shares, address receiver) external returns (uint256);
    function permit(address owner, address spender, uint256 value, uint256 deadline, uint8 v, bytes32 r, bytes32 s) external ;
    function redeem(uint256 shares, address receiver, address owner) external returns (uint256);
    function setFeeRecipient(address _feeRecipient) external ;
    function setPause(bool flag) external ;
    function transfer(address to, uint256 amount) external returns (bool);
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function transferOwnership(address newOwner) external ;
    function withdraw(uint256 assets, address receiver, address owner) external returns (uint256);
}

ghost mapping(address => mapping(uint => uint)) ghostSLoad {
    init_state axiom forall address _executingContract. forall uint _slot. ghostSLoad[_executingContract][_slot] == 0;
}

hook ALL_SLOAD(uint slot) uint val {
    ghostSLoad[executingContract][slot] = val;
}

rule exploreStuff() {
    bool doFlashLoan;

    env e;
    env e1;

    address _token;
    uint256 amount;
    bytes data;

    address _token1;
    uint256 amount1;
    bytes data1;

    method m;
    calldataarg args;

    bool firstCallIsValid = false;
    bool secondCallIsValid = false;

    if (doFlashLoan) {
        firstCallIsValid = flashLoan(e, callbackReceiver, _token, amount, data);
    } else {
        m(e, args);
    }

    require(_token == _token1);
    require(amount <= amount1);

    // Once we've done a call, we want valid calls to flashLoan to revert
    secondCallIsValid = flashLoan@withrevert(e1, callbackReceiver, _token1, amount1, data1);

    assert(lastReverted, "looking for a call that makes flashLoan revert");
}

rule tryToStop() {
    bool doFlashLoan;

    env e;
    env e1;

    address _token;
    uint256 amount;
    bytes data;

    address _token1;
    uint256 amount1;
    bytes data1;

    method m;
    calldataarg args;

    bool firstCallIsValid = false;
    bool secondCallIsValid = false;

    flashLoan(e, callbackReceiver, _token, amount, data);
    flashLoan(e1, callbackReceiver, _token1, amount1, data1);
    
    if (doFlashLoan) {
        firstCallIsValid = flashLoan(e, callbackReceiver, _token, amount, data);
    } else {
        m(e, args);
    }

    require(_token == _token1);
    require(amount <= amount1);

    // Once we've done a call, we want valid calls to flashLoan to revert
    secondCallIsValid = flashLoan@withrevert(e1, callbackReceiver, _token1, amount1, data1);

    assert(lastReverted, "looking for a call that makes flashLoan revert");
}