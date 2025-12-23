import "storageGhost.spec";

methods {
    function _.decimals() external => DISPATCH(optimistic=true)[SimpleToken.decimals()];
    function _.balanceOf(address) external => DISPATCH(optimistic=true)[SimpleToken._];
    function _.transfer(address to, uint256 amount) external => DISPATCH(optimistic=true)[SimpleToken._];
    function _.transferFrom(address from, address to, uint256 amount) external => DISPATCH(optimistic=true)[SimpleToken._];
    function _.approve(address spender, uint256 amount) external => DISPATCH(optimistic=true)[SimpleToken._];
    function UnstoppableVault_Harness.isLockedBySoladyReentrancyGuard() external returns (bool) envfree;
}

// invariant reentracyAlwaysResets()
//     !isLockedBySoladyReentrancyGuard();

rule x() {
    require(currentContract.getCodesize() != assert_uint256(currentContract), "codesize and the contract address cant be the same");
    require(!isLockedBySoladyReentrancyGuard(), "cannot start in a locked state");

    assert(currentContract.shark() > 0, "shark must be gt 0");

    assert(!isLockedBySoladyReentrancyGuard(), "cannot end in a locked state");
}
