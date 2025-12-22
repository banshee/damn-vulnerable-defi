import "SoladyReentrancyGuardHelper.spec";

methods {
    function ReentrancyGuardDemo.getSoladyCodesize() external returns (uint256) envfree;
    function ReentrancyGuardDemo.shark() external returns (bool) envfree;

    // view
    function ReentrancyGuardDemo.getSoladyReentrancyGuardValue() external returns (uint256) envfree;
    function ReentrancyGuardDemo.isLockedBySoladyReentrancyGuard() external returns (bool) envfree;
}

use invariant reentracyLockIsUnlockedAtStartAndEnd;
