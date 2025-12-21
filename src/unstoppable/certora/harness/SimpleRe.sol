// SPDX-License-Identifier: MIT
// Damn Vulnerable DeFi v4 (https://damnvulnerabledefi.xyz)
pragma solidity ^0.8.25;

import {ReentrancyGuard} from "solady/utils/ReentrancyGuard.sol";
import {FixedPointMathLib} from "solmate/utils/FixedPointMathLib.sol";
import {Owned} from "solmate/auth/Owned.sol";
import {SafeTransferLib, ERC4626, ERC20} from "solmate/tokens/ERC4626.sol";
import {Pausable} from "@openzeppelin/contracts/utils/Pausable.sol";
import {IERC3156FlashBorrower, IERC3156FlashLender} from "@openzeppelin/contracts/interfaces/IERC3156.sol";
import {UnstoppableVault} from "src/unstoppable/UnstoppableVault.sol";
import {SoladyReentrancyGuardHelper} from "src/unstoppable/certora/harness/SoladyReentrancyGuardHelper.sol";

/**
 * An ERC4626-compliant tokenized vault offering flashloans for a fee.
 * An owner can pause the contract and execute arbitrary changes.
 */
contract SimpleRe is ReentrancyGuard, SoladyReentrancyGuardHelper {
    function shark() external nonReentrant returns (bool) {
        return true;
    }

    function getCodesize() public pure returns (uint256 s) {
        assembly {
            s := codesize()
        }
    }
}
