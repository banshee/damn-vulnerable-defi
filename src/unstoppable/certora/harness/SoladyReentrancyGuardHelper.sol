// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import {SoladyReentrancyGuardHelperLib} from "src/unstoppable/certora/harness/lib/SoladyReentrancyGuardHelperLib.sol";
import {ReentrancyGuard} from "solady/utils/ReentrancyGuard.sol";

contract SoladyReentrancyGuardHelper {
    function isLockedBySoladyReentrancyGuard() external view returns (bool) {
        // Call the library function directly
        return SoladyReentrancyGuardHelperLib.isLocked();
    }

    function getSoladyReentrancyGuard() external view returns (uint256) {
        // Call the library function directly
        return SoladyReentrancyGuardHelperLib.getReentrancyGuardStatus();
    }
}