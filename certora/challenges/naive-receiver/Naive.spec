import "../../spec/equality.spec";

using WETH as weth;
using NaiveReceiverPool as nrp;
using BasicForwarder as forwarder;
using FlashLoanReceiver as flReceiver;

methods {
    // view
    function NaiveReceiverPool.deposits(address) external returns (uint256) envfree;
    function NaiveReceiverPool.feeReceiver() external returns (address) envfree;
    function NaiveReceiverPool.flashFee(address token, uint256) external returns (uint256) envfree;
    function NaiveReceiverPool.maxFlashLoan(address token) external returns (uint256) envfree;
    function NaiveReceiverPool.totalDeposits() external returns (uint256) envfree;
    function NaiveReceiverPool.trustedForwarder() external returns (address) envfree;
    function NaiveReceiverPool.weth() external returns (address) envfree;

    function WETH.balanceOf(address) external returns (uint256) envfree;
}

rule cannotChangeBalances(method f) {
    address player;

    env e;
    calldataarg args;

    require currentContract == nrp, "basic setup";
    require nrp.weth() == weth, "basic setup";
    require nrp.trustedForwarder() == forwarder, "basic setup";

    address feeReceiver = nrp.feeReceiver(); // note that the test has feeReceiver == deployer, and deployer has the initial WETH deposit

    require notEqualAndNotZero6(player, weth, forwarder, flReceiver, nrp, feeReceiver), "different addresses";

    require forall address a. (a == flReceiver || a == nrp) ? weth.balanceOf[a] < 2 ^ 180 : weth.balanceOf[a] == 0, "only receiver and the pool have weth per test/naive-receiver/NaiveReceiver.t.sol";
    require forall address a. weth.allowance[a][player] == 0 && weth.allowance[a][forwarder] == 0, "player and forwarder have no allowances";
    require forall address a. nrp.deposits[a] == (a == feeReceiver ? weth.balanceOf[nrp] : 0), "only feeReceiver/deployer has pool deposit";
    require forall address a. nativeBalances[a] == (a == weth ? weth.balanceOf[nrp] : 0), "only weth has native eth";

    mathint receiverBalanceBefore = weth.balanceOf(flReceiver);
    mathint poolBalanceBefore = weth.balanceOf(nrp);

    require e.msg.sender == player || e.msg.sender == forwarder, "try as player and forwarder";

    f(e, args);

    mathint receiverBalanceChange = weth.balanceOf(flReceiver) - receiverBalanceBefore;
    mathint poolBalanceChange = weth.balanceOf(nrp) - poolBalanceBefore;

    assert poolBalanceChange >= 0, "cannot pull funds out of pool";
    assert receiverBalanceChange >= 0, "cannot pull funds out of flash loan receiver";
}
