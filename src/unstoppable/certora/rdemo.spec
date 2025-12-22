import "storageGhost.spec";

using SmallContract as sc;

methods {
    function ReentrancyGuardDemo.isLocked() external returns (bool) envfree;
    function ReentrancyGuardDemo.shark() external returns (bool) envfree;
    function ReentrancyGuardDemo.getSoladyReentrancyGuardValue() external returns (uint256) envfree;
    function ReentrancyGuardDemo.getCodesize() external returns (uint256) envfree;
    function ReentrancyGuardDemo.guardValueInsideCall() external returns (uint256) envfree;

    // nonpayable
    function SmallContract.doNothing() external returns (bool) envfree;
    function SmallContract.updateVX() external returns (bool) envfree;

    // pure
    function SmallContract.getCodesize() external returns (uint256) envfree;

    // view
    function SmallContract.v1() external returns (uint256) envfree;
    function SmallContract.v2() external returns (uint256) envfree;
}

invariant reentracyLockIsUnlockedAtStartAndEnd()
    currentContract.getCodesize() != assert_uint256(currentContract) && (!(getSoladyReentrancyGuardValue() == assert_uint256(currentContract)))
    {
        preserved constructor() {
            require(currentContract.getCodesize() != assert_uint256(currentContract), "guard won't work if codesize is the same as address");
            require(currentContract.getSoladyReentrancyGuardValue() == 0, "guard must be zero at startup");
        }
    }

rule x() {
    requireInvariant reentracyLockIsUnlockedAtStartAndEnd();

    // require(currentContract.getCodesize() != assert_uint256(currentContract), "guard will work if codesize is the same as address");
    // require(!currentContract.isLocked(), "cannot start in a locked state");

    assert(currentContract.shark(), "shark must be true");

    // After a call, the reentrancy guard should be unlocked
    assert(currentContract.getSoladyReentrancyGuardValue() == currentContract.getCodesize(), "codesize means unlocked");
    assert(currentContract.guardValueInsideCall() == assert_uint256(currentContract), "address means locked and it should have been locked during the call");

    assert(!currentContract.isLocked(), "cannot end in a locked state");
}

invariant smallContractCodesize()
    sc.v1() == sc.v2();

rule y() {
    assert(sc.v1() == sc.v2());
}
