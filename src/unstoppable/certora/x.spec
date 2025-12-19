import "storageGhost.spec";

methods {
    function _.decimals() external => DISPATCHER(true);
    function _.balanceOf(address) external => DISPATCHER(true);
    function _.transfer(address to, uint256 amount) external => DISPATCHER(true);
    function _.transferFrom(address from, address to, uint256 amount) external => DISPATCHER(true);
    function _.approve(address spender, uint256 amount) external => DISPATCHER(true);
    function UnstoppableVault_Harness.isLockedBySoladyReentrancyGuard() external returns (bool) envfree;
}

// invariant reentracyAlwaysResets()
//     !isLockedBySoladyReentrancyGuard();

rule x() {
    require(!isLockedBySoladyReentrancyGuard(), "cannot start in a locked state");

    env e;
    calldataarg args;
    currentContract.mint(e, args);

    assert (!isLockedBySoladyReentrancyGuard(), "cannot end in a locked state");
}