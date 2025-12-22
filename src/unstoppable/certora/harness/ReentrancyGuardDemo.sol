// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import {SoladyReentrancyGuardHelper} from "./SoladyReentrancyGuardHelper.sol";

/// Hacked version of Solady, just to demo a problem:
/// @notice Reentrancy guard mixin.
/// @author Solady (https://github.com/vectorized/solady/blob/main/src/utils/ReentrancyGuard.sol)

// guard value is either contract codesize (unlocked) or contract address (locked), or zero (uninitialized)
contract ReentrancyGuardDemo is SoladyReentrancyGuardHelper {
    function shark() public pure returns (bool){
        return true;
    }
}