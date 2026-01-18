import "SimpleToken.spec";
import "SimpleTokenDispatch.spec";

using UnstoppableVault_Harness as UnstoppableVaultToken1;

methods {
    function UnstoppableVaultToken1.balanceOf(address account) external returns (uint256) envfree;
    function UnstoppableVaultToken1.totalSupply() external returns (uint256) envfree;
    function _.onFlashLoan(address initiator, address token, uint256 amount, uint256 fee, bytes data) external => DISPATCH(optimistic=true)[UnstoppableVaultToken1.onFlashLoan(address, address, uint256, uint256, bytes)];
}

ghost mapping(address => uint256) ghostBalancesUnstoppableVaultToken1;

hook Sstore UnstoppableVaultToken1.balanceOf[KEY address addr] uint256 newValue (uint256 oldValue) {
    // we're not interested in overflows for this entire proof.  The test environment only cares about
    // a setup where totalSupply is set to 1 million tokens.
    require(SimpleTokenToken1.balanceOf(UnstoppableVaultToken1) + newValue < max_uint64, "overflow guard");
    sumOfBalancesUnstoppableVaultToken1 = sumOfBalancesUnstoppableVaultToken1 + newValue - oldValue;
    ghostBalancesUnstoppableVaultToken1[addr] = newValue;
}

function matchingTokenAndBalance() returns bool {
    return UnstoppableVaultToken1.asset == SimpleTokenToken1 && SimpleTokenToken1.totalSupply() < max_uint64;
}

invariant ghostMatchesStorageUnstoppableVaultToken1(address user)
    matchingTokenAndBalance() && ghostBalancesUnstoppableVaultToken1[user] == UnstoppableVaultToken1.balanceOf(user)
    filtered {
        f -> f.selector != sig:execute(address,bytes).selector
    }
    {
        preserved constructor() {
            require (matchingTokenAndBalance() , "matching token and balance condition");
            require(forall address a. ghostBalancesUnstoppableVaultToken1[a] == 0, "all zero ghost balances");
        }
    }

invariant totalSupplyIsSumOfBalancesUnstoppableVaultToken1()
    matchingTokenAndBalance() && UnstoppableVaultToken1.totalSupply() == sumOfBalancesUnstoppableVaultToken1 && UnstoppableVaultToken1.totalSupply() < max_uint64
    {
        preserved constructor() {
            require (matchingTokenAndBalance() , "matching token and balance condition");
            require(sumOfBalancesUnstoppableVaultToken1 == 0, "sum of balances starts at zero");
        }
    }

function requireAllInvariantsUnstoppableVaultToken1() {
    address a;
    requireInvariant ghostMatchesStorageUnstoppableVaultToken1(a);
    requireInvariant totalSupplyIsSumOfBalancesUnstoppableVaultToken1();
}
