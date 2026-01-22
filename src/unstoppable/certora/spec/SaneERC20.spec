ghost mapping(address => mathint) mirrorBalances {
    init_state axiom (forall address a. mirrorBalances[a] == 0) && (usum address a. mirrorBalances[a]) == 0;
}

hook Sstore currentContract.balances[KEY address a] uint256 newVal {
    mirrorBalances[a] = newVal;
}

hook Sload uint256 val currentContract.balances[KEY address a] {
    require mirrorBalances[a] == val, "mirror balance matches loaded value";
}

invariant totalSupplyIsSumOfBalances()
    currentContract.totalSupply == (usum address a. mirrorBalances[a]);
    
invariant balancesMatch(address a)
    mirrorBalances[a] == currentContract.balances[a];
