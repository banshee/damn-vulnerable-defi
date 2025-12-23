import "SoladyReentrancyGuardHelper.spec";

methods {
    // pure
    function ReentrancyGuardDemo.getSoladyCodesize() external returns (uint256) envfree;

    // view
    function ReentrancyGuardDemo.getSoladyReentrancyGuardValue() external returns (uint256) envfree;
    function ReentrancyGuardDemo.isLockedBySoladyReentrancyGuard() external returns (bool) envfree;

    // nonpayable
    function ReentrancyGuardDemo.shark() external returns (uint256) envfree;
}

use invariant reentracyLockIsUnlocked;
