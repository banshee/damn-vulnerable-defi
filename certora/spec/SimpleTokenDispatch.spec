methods {
    // view
    function SimpleToken.allowance(address owner, address spender) external returns (uint256) envfree;
    function SimpleToken.balanceOf(address account) external returns (uint256) envfree;
    function SimpleToken.decimals() external returns (uint8) envfree;
    function SimpleToken.name() external returns (string) envfree;
    function SimpleToken.symbol() external returns (string) envfree;
    function SimpleToken.totalSupply() external returns (uint256) envfree;
    // nonpayable
    // function SimpleToken.approve(address spender, uint256 value) external returns (bool) envfree;
    // function SimpleToken.transfer(address to, uint256 value) external returns (bool) envfree;
    // function SimpleToken.transferFrom(address from, address to, uint256 value) external returns (bool) envfree;
    
    // view
    function _.allowance(address owner, address spender) external => DISPATCH(optimistic=true)[SimpleToken.allowance(address, address)];
    function _.balanceOf(address account) external => DISPATCH(optimistic=true)[SimpleToken.balanceOf(address)];
    function _.decimals() external => DISPATCH(optimistic=true)[SimpleToken.decimals()];
    function _.name() external => DISPATCH(optimistic=true)[SimpleToken.name()];
    function _.symbol() external => DISPATCH(optimistic=true)[SimpleToken.symbol()];
    function _.totalSupply() external => DISPATCH(optimistic=true)[SimpleToken.totalSupply()];
    // nonpayable
    function _.approve(address spender, uint256 value) external => DISPATCH(optimistic=true)[SimpleToken.approve(address, uint256)];
    function _.transfer(address to, uint256 value) external => DISPATCH(optimistic=true)[SimpleToken.transfer(address, uint256)];
    function _.transferFrom(address from, address to, uint256 value) external => DISPATCH(optimistic=true)[SimpleToken.transferFrom(address, address, uint256)];
}