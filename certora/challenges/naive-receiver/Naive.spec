import "../../spec/equality.spec";

using WETH as weth;
using NaiveReceiverPool as nrp;
using BasicForwarder as forwarder;
using FlashLoanReceiver as flReceiver;
using BasicForwarderExecuteWrapper as wrapper;

methods {
    // payable
    function NaiveReceiverPool.deposit() external;

    // view
    function NaiveReceiverPool.deposits(address) external returns (uint256) envfree;
    function NaiveReceiverPool.feeReceiver() external returns (address) envfree;
    function NaiveReceiverPool.flashFee(address token, uint256) external returns (uint256) envfree;
    function NaiveReceiverPool.maxFlashLoan(address token) external returns (uint256) envfree;
    function NaiveReceiverPool.totalDeposits() external returns (uint256) envfree;
    function NaiveReceiverPool.trustedForwarder() external returns (address) envfree;
    function NaiveReceiverPool.weth() external returns (address) envfree;

    // nonpayable
    function NaiveReceiverPool.flashLoan(address receiver, address token, uint256 amount, bytes data) external returns (bool);
    function NaiveReceiverPool.multicall(bytes[] data) external returns (bytes[]) envfree;
    function NaiveReceiverPool.withdraw(uint256 amount, address receiver) external;

    function WETH.balanceOf(address) external returns (uint256) envfree;

    function _.execute(BasicForwarder.Request, bytes) external => DISPATCHER(true);
}

rule cannotIncreaseBalance(method f) {
    address player;

    env e;
    calldataarg args;

    require currentContract == nrp;
    require nrp.weth() == weth, "basic setup";
    require nrp.trustedForwarder() == forwarder, "basic setup";
    require nrp.feeReceiver() == flReceiver, "basic setup";

    notEqualAndNotZero4(player, weth, forwarder, flReceiver);
    require nativeBalances[player] == 0, "player has no eth to turn into WETH";

    mathint balanceBefore = weth.balanceOf(player);
    // f(e, args);
    BasicForwarder.Request r;
    bytes sigbytes;
    bool b = wrapper.executeWrapper(e, r, forwarder, to_bytes4(sig:BasicForwarder.basicStuff().selector), forwarder);
    assert b, "asdf";

    mathint balanceAfter = weth.balanceOf(player);

    assert balanceBefore <= balanceAfter, "player balance cannot increase";
}

// BasicForwarder.Request memory myRequest = BasicForwarder.Request({
//     from: 0xYourAddress,           // The account signing the request
//     target: 0xdeadbeef,            // The target contract
//     value: 0,                      // Assuming no ETH is sent
//     gas: 100000,                   // Adjust as needed
//     nonce: currentNonce,           // Get this from forwarder.nonces(0xYourAddress)
//     data: abi.encodeWithSelector(0x7ecebe00), // Just the selector!
//     deadline: block.timestamp + 1 hours
// });
