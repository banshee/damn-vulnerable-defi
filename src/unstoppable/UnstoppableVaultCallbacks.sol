// SPDX-License-Identifier: MIT
// Damn Vulnerable DeFi v4 (https://damnvulnerabledefi.xyz)
pragma solidity =0.8.25;

import {
    IERC3156FlashBorrower
} from "@openzeppelin/contracts/interfaces/IERC3156.sol";
import {UnstoppableVault} from "./UnstoppableVault.sol";

error BadFunctionChoice();
error BadFunctionCount();

/**
 * An ERC4626-compliant tokenized vault offering flashloans for a fee.
 * An owner can pause the contract and execute arbitrary changes.
 */
contract UnstoppableVaultCallbacks {
    uint256 iteration;
    mapping(uint256 => uint8) functionIds;
    mapping(uint256 => uint8) functionCounts;

    UnstoppableVault callingContract;
    mapping(uint256 => address) parameters_address;
    mapping(uint256 => uint256) parameters_uint256;
    mapping(uint256 => bytes32) parameters_bytes32;

    constructor(UnstoppableVault _callingContract) {
        callingContract = _callingContract;
    }

    function doCallback() internal {
        uint256 functionId = functionIds[iteration];
        if (functionId > 1) {
            revert BadFunctionChoice();
        }
        if (functionId == 0) {
            callingContract.approve(
                parameters_address[iteration + 0],
                parameters_uint256[iteration + 1]
            );
            iteration += 2;
        } else if (functionId == 1) {
            callingContract.deposit(
                parameters_uint256[iteration + 0],
                parameters_address[iteration + 1]
            );
            iteration += 2;
        }
    }
    function doNCallbacks() public {
        uint256 functionCount = functionCounts[iteration];
        iteration += 1;
        if (functionCount > 3) {
            revert BadFunctionCount();
        }
        if (functionCount <= 0) {
            return;
        }
        if (functionCount <= 1) {
            doCallback();
        }
        if (functionCount <= 2) {
            doCallback();
        }
        if (functionCount <= 3) {
            doCallback();
        }
    }
}
