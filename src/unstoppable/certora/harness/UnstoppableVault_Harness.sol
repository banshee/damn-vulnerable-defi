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
contract UnstoppableVault_Harness is
    UnstoppableVault,
    SoladyReentrancyGuardHelper
{
    using FixedPointMathLib for uint256;

    constructor(
        ERC20 _token,
        address _owner,
        address _feeRecipient
    ) UnstoppableVault(_token, _owner, _feeRecipient) {}

    function flashFeeAdjustedForBug(
        address _token,
        uint256 _amount
    ) public view returns (uint256 fee) {
        if (address(asset) != _token) {
            revert UnsupportedCurrency();
        }

        // The bug in flashFee() is that calcules the fee AFTER loaning the
        // money to receipient, so the receipient might have their fee subsidy eligibility
        // stolen.  The calculation should be before doing the actual loan.
        uint256 adjustedMaxFlashloan = ERC20(_token).balanceOf(address(this)) -
            _amount;

        if (block.timestamp < end && _amount < adjustedMaxFlashloan) {
            return 0;
        } else {
            return _amount.mulWadUp(FEE_FACTOR);
        }
    }
}
