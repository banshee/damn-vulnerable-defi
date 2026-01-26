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
    uint256 lastLock;

    function lockShouldBeTrue() external nonReentrant returns (bool) {
        // This will be true because we are inside nonReentrant
        return this.isLockedBySoladyReentrancyGuard();
    }

    function lockShouldBeFalse() external view returns (bool) {
        // This will be false because we are not inside nonReentrant
        return this.isLockedBySoladyReentrancyGuard();
    }

    function lockValue() external nonReentrant returns (uint256) {
        // This should be address(this) because we are inside nonReentrant
        lastLock = this.getSoladyReentrancyGuardValue();
        return lastLock;
    }
}

contract ReentrantGuard is Test {
    function setUp() public {}

    function test_WithHelper_isLocked() public {
        WithHelper helper = new WithHelper();
        assertFalse(helper.isLockedBySoladyReentrancyGuard());
    }

    function test_WithHelper_reentrantLock() public {
        WithHelper helper = new WithHelper();
        assertEq(helper.getSoladyReentrancyGuardValue(), 0);
        bytes memory bytecode = vm.getDeployedCode("sample.t.sol:WithHelper");
        uint256 codeSize = bytecode.length;
        assertTrue(
            helper.lockShouldBeTrue(),
            "Lock should be true inside reentrant code"
        );
        assertEq(
            helper.getSoladyReentrancyGuardValue(),
            codeSize,
            "guard shall be codeSize"
        );
    }

    function test_WithHelper_nonReentrantLock() public {
        WithHelper helper = new WithHelper();
        assertFalse(
            helper.lockShouldBeFalse(),
            "Lock should be false for non-reentrant code"
        );
    }
}
