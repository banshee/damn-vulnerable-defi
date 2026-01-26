using SimpleToken as Token1;

methods {
    function Token1.totalSupply() external returns (uint256) envfree;
}

ghost mapping(address => uint256) ghostBalancesToken1 {
    init_state axiom (forall address a. ghostBalancesToken1[a] == 0) && (usum address a. ghostBalancesToken1[a]) == 0;
}

hook Sstore Token1._balances[KEY address addr] uint256 newValue (uint256 oldValue) {
    ghostBalancesToken1[addr] = newValue;
}

hook Sload uint256 val Token1._balances[KEY address a] {
    require ghostBalancesToken1[a] == val;
}

invariant ghostMatchesStorageToken1(address user)
    ghostBalancesToken1[user] == Token1._balances[user];

invariant totalSupplyIsSumOfBalancesToken1()
    Token1.totalSupply() == (usum address a. ghostBalancesToken1[a]);

function requireAllInvariantsToken1() {
    address a;
    requireInvariant ghostMatchesStorageToken1(a);
    requireInvariant totalSupplyIsSumOfBalancesToken1();
}
