using DamnValuableToken as asset;
using UnstoppableVault as vault;

ghost mapping(address => mathint) mirrorBalances_asset {
    init_state axiom (forall address a. mirrorBalances_asset[a] == 0) && (usum address a. mirrorBalances_asset[a]) == 0;
}

hook Sstore asset.balanceOf[KEY address a] uint256 newVal {
    mirrorBalances_asset[a] = newVal;
}

hook Sload uint256 val asset.balanceOf[KEY address a] {
    require mirrorBalances_asset[a] == val, "mirror balance matches loaded value";
}

invariant totalSupplyIsSumOfBalances_asset()
    asset.totalSupply == (usum address a. mirrorBalances_asset[a]);
    
invariant balancesMatch_asset(address a)
    mirrorBalances_asset[a] == asset.balanceOf[a];

function requireAllInvariants_asset() {
    address a;
    requireInvariant balancesMatch_asset(a);
    requireInvariant totalSupplyIsSumOfBalances_asset();
}

ghost mapping(address => mathint) mirrorBalances_vault {
    init_state axiom (forall address a. mirrorBalances_vault[a] == 0) && (usum address a. mirrorBalances_vault[a]) == 0;
}

hook Sstore vault.balanceOf[KEY address a] uint256 newVal {
    mirrorBalances_vault[a] = newVal;
}

hook Sload uint256 val vault.balanceOf[KEY address a] {
    require mirrorBalances_vault[a] == val, "mirror balance matches loaded value";
}

invariant totalSupplyIsSumOfBalances_vault()
    vault.totalSupply == (usum address a. mirrorBalances_vault[a]);
    
invariant balancesMatch_vault(address a)
    mirrorBalances_vault[a] == vault.balanceOf[a];

function requireAllInvariants_vault() {
    address a;
    requireInvariant balancesMatch_vault(a);
    requireInvariant totalSupplyIsSumOfBalances_vault();
}

function requireAllErc20Invariants() {
    requireAllInvariants_asset();
    requireAllInvariants_vault();
}