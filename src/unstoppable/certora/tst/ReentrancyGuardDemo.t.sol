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
        uint256 currentContractAddress = uint256(uint160(address(currentContract)));
        assertEq(currentContract.getReentrancyGuardValue(), 0, "storage initialized to zero");
        assertFalse(currentContract.isLocked(), "must start out unlocked");
        assertTrue(currentContract.shark(), "make a call that just returns true, we only care about reentrancy guard");
        assertEq(currentContract.guardValueInsideCall(), currentContractAddress, "inside call, guard value should be contract address");
        assertEq(currentContract.getReentrancyGuardValue(), vm.getDeployedCode("ReentrancyGuardDemo.sol:ReentrancyGuardDemo").length, "after call should be codesize");
        assertFalse(currentContract.isLocked());
    }
}
