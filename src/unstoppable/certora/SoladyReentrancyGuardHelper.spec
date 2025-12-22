import "storageGhost.spec";

// methods {
//     // pure
//     function SoladyReentrancyGuardHelper.getSoladyCodesize() external returns (uint256) envfree;

//     // view
//     function SoladyReentrancyGuardHelper.getSoladyReentrancyGuardValue() external returns (uint256) envfree;
//     function SoladyReentrancyGuardHelper.isLockedBySoladyReentrancyGuard() external returns (bool) envfree;
// }

function lockStateIsValid() returns (bool) {
  return currentContract.getSoladyCodesize() != assert_uint256(currentContract) && !isLockedBySoladyReentrancyGuard();
}

invariant reentracyLockIsUnlockedAtStartAndEnd()
    lockStateIsValid();