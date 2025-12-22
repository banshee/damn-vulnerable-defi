import "storageGhost.spec";
import "SimpleTokenDispatch.spec";

methods {
    function UnstoppableVault_Harness.isLockedBySoladyReentrancyGuard() external returns (bool) envfree;
    function UnstoppableVault_Harness.getSoladyCodesize() external returns (uint256) envfree;
    function UnstoppableVault_Harness.getSoladyReentrancyGuardValue() external returns (uint256) envfree;
}

invariant reentracyAlwaysResets()
    getSoladyReentrancyGuardValue() != 0 && getSoladyCodesize() != assert_uint256(currentContract) && !isLockedBySoladyReentrancyGuard();

// rule x() {
//     requireInvariant reentracyAlwaysResets();

//     assert(currentContract.shark(), "shark must be true");
// }
