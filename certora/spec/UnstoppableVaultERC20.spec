ghost mapping(address => mathint) mirrorBalances_UnstoppableVaultERC20Setup {
    init_state axiom (forall address a. mirrorBalances_UnstoppableVaultERC20Setup[a] == 0) && (usum address a. mirrorBalances_UnstoppableVaultERC20Setup[a]) == 0;
}

hook Sstore UnstoppableVaultERC20Setup.balances[KEY address a] uint256 newVal {
    mirrorBalances_UnstoppableVaultERC20Setup[a] = newVal;
}

hook Sload uint256 val UnstoppableVaultERC20Setup.balances[KEY address a] {
    require mirrorBalances_UnstoppableVaultERC20Setup[a] == val, "mirror balance matches loaded value";
}

invariant totalSupplyIsSumOfBalances_UnstoppableVaultERC20Setup()
    UnstoppableVaultERC20Setup.totalSupply == (usum address a. mirrorBalances_UnstoppableVaultERC20Setup[a]);
    
invariant balancesMatch_UnstoppableVaultERC20Setup(address a)
    mirrorBalances_UnstoppableVaultERC20Setup[a] == UnstoppableVaultERC20Setup.balances[a];

function requireAllInvariants_UnstoppableVaultERC20Setup() {
    address a;
    requireInvariant balancesMatch_UnstoppableVaultERC20Setup(a);
    requireInvariant totalSupplyIsSumOfBalances_UnstoppableVaultERC20Setup();
}
