using SimpleToken as SimpleTokenToken1;

methods {
    function SimpleTokenToken1.balanceOf(address account) external returns (uint256) envfree;
    function SimpleTokenToken1.totalSupply() external returns (uint256) envfree;
}

ghost mapping(address => uint256) ghostBalancesSimpleTokenToken1 {
    init_state axiom (forall address a. ghostBalancesSimpleTokenToken1[a] == 0) && (usum address a. ghostBalancesSimpleTokenToken1[a]) == 0;
}

hook Sstore SimpleTokenToken1._balances[KEY address addr] uint256 newValue (uint256 oldValue) {
    // mathint nv = newValue;
    // mathint ov = oldValue;
    // mathint newBalance = sumOfBalancesSimpleTokenToken1 + nv - ov;

    // // require(newBalance < max_uint256, "not interested in overflows");
    // sumOfBalancesSimpleTokenToken1 = newBalance;
    ghostBalancesSimpleTokenToken1[addr] = newValue;
}

hook Sload uint256 val SimpleTokenToken1._balances[KEY address a] {
    // mathint nv = newValue;
    // mathint ov = oldValue;
    // mathint newBalance = sumOfBalancesSimpleTokenToken1 + nv - ov;

    // // require(newBalance < max_uint256, "not interested in overflows");
    // sumOfBalancesSimpleTokenToken1 = newBalance;
    require ghostBalancesSimpleTokenToken1[a] == val;
}

invariant ghostMatchesStorageSimpleTokenToken1(address user)
    ghostBalancesSimpleTokenToken1[user] == SimpleTokenToken1._balances[user];

invariant totalSupplyIsSumOfBalancesSimpleTokenToken1()
    SimpleTokenToken1.totalSupply() == (usum address a. ghostBalancesSimpleTokenToken1[a]);

function requireAllInvariantsSimpleTokenToken1() {
    address a;
    requireInvariant ghostMatchesStorageSimpleTokenToken1(a);
    requireInvariant totalSupplyIsSumOfBalancesSimpleTokenToken1();
}
