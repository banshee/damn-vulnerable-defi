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
        return SoladyReentrancyGuardHelperLib.getReentrancyGuardValue();
    }

    // getCodesize is required because certora treats codesize as something that can vary.
    // The Solady reentrancy guard switches between codesize and the contract address
    // so we need to add a require(codesize != address) in the spec.
    function getCodesize() public pure returns (uint256 s) {
        assembly {
            s := codesize()
        }
    }
}
