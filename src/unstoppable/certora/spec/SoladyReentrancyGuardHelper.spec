function lockStateIsValid() returns (bool) {
    return currentContract.getSoladyCodesize() != assert_uint256(currentContract) && !isLockedBySoladyReentrancyGuard();
}

invariant reentracyLockIsUnlocked()
    lockStateIsValid()
    {
        preserved constructor() {
            require(lockStateIsValid(), "constructor has to have CODESIZE different from address");
        }
    }
