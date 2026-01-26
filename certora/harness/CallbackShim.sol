// SPDX-License-Identifier: MIT
// Damn Vulnerable DeFi v4 (https://damnvulnerabledefi.xyz)
pragma solidity =0.8.25;

import {IERC3156FlashBorrower} from "@openzeppelin/contracts/interfaces/IERC3156.sol";
import {UnstoppableVault} from "src/unstoppable/UnstoppableVault.sol";
import {ERC20} from "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import {Callback_UnstoppableVault} from "./Callback_UnstoppableVault.sol";
import {CallbackBase} from "./CallbackBase.sol";

/**
 * An ERC4626-compliant tokenized vault offering flashloans for a fee.
 * An owner can pause the contract and execute arbitrary changes.
 */
contract CallbackShim is CallbackBase, Callback_UnstoppableVault {
    function executePossibleCallbacks() internal override returns (uint256) {
        return doCallback(targetVault, this);
    }
}
