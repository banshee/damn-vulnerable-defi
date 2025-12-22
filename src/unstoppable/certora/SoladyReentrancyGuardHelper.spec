import "storageGhost.spec";

invariant reentracyLockIsUnlockedAtStartAndEnd()
    currentContract.getSoladyCodesize() != assert_uint256(currentContract) && (!(getSoladyReentrancyGuardValue() == assert_uint256(currentContract)))
    {
        preserved constructor() {
            require(currentContract.getSoladyCodesize() != assert_uint256(currentContract), "guard won't work if codesize is the same as address");
            require(currentContract.getSoladyReentrancyGuardValue() == 0, "guard must be zero at startup");
        }
    }
