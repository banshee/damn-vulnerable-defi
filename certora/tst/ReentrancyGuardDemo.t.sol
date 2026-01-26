// SPDX-License-Identifier: UNLICENSED

pragma solidity 0.8.25;

import {Test} from "forge-std/Test.sol";
import {SoladyReentrancyGuardHelperLib} from "src/unstoppable/certora/harness/lib/SoladyReentrancyGuardHelperLib.sol";
import {SoladyReentrancyGuardHelper} from "src/unstoppable/certora/harness/SoladyReentrancyGuardHelper.sol";
import {ReentrancyGuard} from "solady/utils/ReentrancyGuard.sol";
import {ReentrancyGuardDemo} from "src/unstoppable/certora/harness/ReentrancyGuardDemo.sol";

contract ReentrancyGuardDemoTest is Test {
    function setUp() public {}

    function test_shark() public {
        ReentrancyGuardDemo currentContract = new ReentrancyGuardDemo();
        // assertEq(currentContract.getSoladyReentrancyGuardValue(), 0, "storage initialized to zero");
        assertFalse(currentContract.isLockedBySoladyReentrancyGuard(), "must start out unlocked");
        assertTrue(currentContract.shark() > 0, "make a call that just returns true, we only care about reentrancy guard");
    }
}
