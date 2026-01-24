methods {
    function returnCodesize() external returns (uint256) envfree; 
}

invariant checkcodesize()
    currentContract.returnCodesize() == nativeCodesize[currentContract];
