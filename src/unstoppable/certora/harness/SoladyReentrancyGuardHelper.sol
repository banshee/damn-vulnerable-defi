// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import {SoladyReentrancyGuardHelperLib} from "src/unstoppable/certora/harness/lib/SoladyReentrancyGuardHelperLib.sol";
// import {ReentrancyGuard} from "solady/utils/ReentrancyGuard.sol";

abstract contract SoladyReentrancyGuardHelper {
    /// @dev The specific storage slot used by Solady's ReentrancyGuard.
    /// Value: 0x929eee149b4bd21268
    uint256 internal constant _REENTRANCY_GUARD_SLOT = 0x929eee149b4bd21268;

    /// @dev Returns the raw value stored in the guard slot.
    /// Unlocked = contract codesize
    /// Locked = contract address
    function getSoladyReentrancyGuardValue() external view returns (uint256 status) {
        assembly {
            status := sload(_REENTRANCY_GUARD_SLOT)
        }
    }

    /// @dev Helper to return a boolean indicating if the contract is currently locked.
    function isLockedBySoladyReentrancyGuard() external view returns (bool) {
        // Solady sets the slot to address(this) when locked.
        return this.getSoladyReentrancyGuardValue() == uint256(uint160(address(this)));
    }

    // getCodesize is required because certora treats codesize as something that can vary.
    // The Solady reentrancy guard switches between codesize and the contract address
    // so we need to add a require(codesize != address) in the spec.
    function getSoladyCodesize() public pure returns (uint256 s) {
        assembly {
            s := codesize()
        }
    }
}
