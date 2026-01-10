using SimpleToken as token1;

methods {
    function token1.balanceOf(address account) external returns (uint256) envfree;
    function token1.totalSupply() external returns (uint256) envfree;
}

ghost mapping(address => uint256) ghostBalancesToken1;

ghost mathint sumOfBalancesToken1;

hook Sstore token1._balances[KEY address addr] uint256 newValue (uint256 oldValue) {
    sumOfBalancesToken1 = sumOfBalancesToken1 + newValue - oldValue;
    ghostBalancesToken1[addr] = newValue;
}

invariant ghostMatchesStorageToken1(address user)
    ghostBalancesToken1[user] == token1.balanceOf(user)
    {
        preserved constructor() {
            require(forall address a. ghostBalancesToken1[a] == 0, "all zero ghost balances");
        }
    }

invariant totalSupplyIsSumOfBalancesToken1()
    token1.totalSupply() == sumOfBalancesToken1
    {
        preserved constructor() {
            require(sumOfBalancesToken1 == 0, "sum of balances starts at zero");
        }
    }

function requireAllInvariantsToken1() {
    address a;
    requireInvariant ghostMatchesStorageToken1(a);
    requireInvariant totalSupplyIsSumOfBalancesToken1();
}
