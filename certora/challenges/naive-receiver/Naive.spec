using WETH as weth;
using NaiveRecieverPool as nrp;
using BasicForwarder as forwarder;
using FlashLoanReceiver as receiver;

rule something() {
    assert false, "fail here";
}

rule cannotIncreaseBalance(method f) {
    env e;
    calldata data;

    require nrp.weth == weth, "basic setup";
    require nrp.trustedForwarder == forwarder, "basic setup";
    require nrp.receiver == receiver, "basic setup";

    mathint balanceBefore = weth.balanceOf(player);
    f(e, data);
    mathint balanceAfter = weth.balanceOf(player);

    assert(balanceBefore <= balanceAfter);
}