using UnstoppableVault as vault;
using SimpleToken as simpleToken;
using CallbackNoop as receiver;

rule safeTransferFrom() {
    env e;
    address from;
    address to;
    uint256 amount;

    require(amount > currentContract.balanceOf(e, from), "from account must not have enough balance, transfer should fail");
    currentContract.reproSafeTransferFromHavoc(e, to, amount);
    assert(false, "meaningless assert, we just want to see if reproSafeTransferFromHavoc havocs when it should not");
}
