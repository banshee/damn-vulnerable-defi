// SPDX-License-Identifier: UNLICENSED

pragma solidity 0.8.25;

import {Test} from "forge-std/Test.sol";
import {SoladyReentrancyGuardHelperLib} from "src/unstoppable/certora/harness/lib/SoladyReentrancyGuardHelperLib.sol";
import {SoladyReentrancyGuardHelper} from "src/unstoppable/certora/harness/SoladyReentrancyGuardHelper.sol";
import {ReentrancyGuard} from "solady/utils/ReentrancyGuard.sol";
import {UnstoppableVault_Harness} from "src/unstoppable/certora/harness/UnstoppableVault_Harness.sol";
import {UnstoppableVault} from "src/unstoppable/UnstoppableVault.sol";
import {SafeTransferLib, ERC4626, ERC20} from "solmate/tokens/ERC4626.sol";

contract WithHelper is SoladyReentrancyGuardHelper, ReentrancyGuard {
    function lockShouldBeTrue() external nonReentrant returns (bool) {
        // This will be true because we are inside nonReentrant
        return SoladyReentrancyGuardHelperLib.isLocked();
    }

    function lockShouldBeFalse() external view returns (bool) {
        // This will be false because we are not inside nonReentrant
        return SoladyReentrancyGuardHelperLib.isLocked();
    }
}

contract ContractBTest is Test {
    uint256 testNumber;

    function setUp() public {
        testNumber = 42;
    }

    function test_NumberIs42() public view {
        assertEq(testNumber, 42);
    }

    function test_WithHelper_isLocked() public {
        WithHelper helper = new WithHelper();
        assertFalse(helper.isLockedBySoladyReentrancyGuard());
    }

    function test_WithHelper_reentrantLock() public {
        WithHelper helper = new WithHelper();
        assertEq(helper.getSoladyReentrancyGuard(), 0);
        bytes memory bytecode = vm.getCode("sample.t.sol:WithHelper");
        uint256 codeSize = bytecode.length;
        assertTrue(
            helper.lockShouldBeTrue(),
            "Lock should be true inside reentrant code"
        );
        assertEq(helper.getSoladyReentrancyGuard(), codeSize);
    }

    function test_WithHelper_nonReentrantLock() public {
        WithHelper helper = new WithHelper();
        assertFalse(
            helper.lockShouldBeFalse(),
            "Lock should be false for non-reentrant code"
        );
    }
}
