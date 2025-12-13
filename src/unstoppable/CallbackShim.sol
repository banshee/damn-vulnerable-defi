// SPDX-License-Identifier: MIT
// Damn Vulnerable DeFi v4 (https://damnvulnerabledefi.xyz)
pragma solidity =0.8.25;

import {
    IERC3156FlashBorrower
} from "@openzeppelin/contracts/interfaces/IERC3156.sol";
import {Callback_UnstoppableVault} from "./Callback_UnstoppableVault.sol";
import {UnstoppableVault} from "./UnstoppableVault.sol";

/**
 * An ERC4626-compliant tokenized vault offering flashloans for a fee.
 * An owner can pause the contract and execute arbitrary changes.
 */
contract CallbackShim is IERC3156FlashBorrower, Callback_UnstoppableVault {
    UnstoppableVault public immutable targetVault;

    bytes32 public constant RETURN_VALUE =
        keccak256("ERC3156FlashBorrower.onFlashLoan");

    function onFlashLoan(
        address,
        address,
        uint256,
        uint256,
        bytes calldata
    ) external override returns (bytes32) {
        doCallback(targetVault);
        return RETURN_VALUE;
    }
}
