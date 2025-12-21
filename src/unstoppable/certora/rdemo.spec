import "storageGhost.spec";

methods {
    function ReentrancyGuardDemo.isLocked() external returns (bool) envfree;
    function ReentrancyGuardDemo.shark() external returns (bool) envfree;
    function ReentrancyGuardDemo.getReentrancyGuardValue() external returns (uint256) envfree;
    function ReentrancyGuardDemo.getCodesize() external returns (uint256) envfree;
    function ReentrancyGuardDemo.guardValueInsideCall() external returns (uint256) envfree;
}

// invariant reentracyAlwaysResets()
//     !isLockedBySoladyReentrancyGuard();

rule x() {
    require(currentContract.getCodesize() != assert_uint256(currentContract), "nothing will work if codesize is the same as address");
    require(!currentContract.isLocked(), "cannot start in a locked state");

    assert(currentContract.shark(), "shark must be true");

    // After a call, the reentrancy guard should be unlocked
    assert(currentContract.getReentrancyGuardValue() == currentContract.getCodesize(), "codesize means unlocked");
    assert(currentContract.guardValueInsideCall() == assert_uint256(currentContract), "address means locked and it should have been locked during the call");

    assert(!currentContract.isLocked(), "cannot end in a locked state");
}
