// SPDX-License-Identifier: MIT 
pragma solidity =0.8.25;

import {
    IERC3156FlashBorrower
} from "@openzeppelin/contracts/interfaces/IERC3156.sol";
import {UnstoppableVault} from "./UnstoppableVault.sol";

error BadFunctionChoice();
error BadFunctionCount();

contract UnstoppableVaultCallbacks {
    uint256 iteration;
    mapping(uint256 => uint8) functionIds;
    mapping(uint256 => uint8) functionCounts;

    mapping(uint256 => address) parameters_address;
    mapping(uint256 => uint256) parameters_uint256;
    mapping(uint256 => bytes32) parameters_bytes32;

    function doCallback(UnstoppableVault callingContract) internal {
        uint256 functionId = functionIds[iteration++];
        if (functionId > 1) {
            revert BadFunctionChoice();
        }
        if (functionId == 0) {
            callingContract.approve(
                parameters_address[iteration++],
                parameters_uint256[iteration++]
            );
        } else if (functionId == 1) {
            callingContract.deposit(
                parameters_uint256[iteration++],
                parameters_address[iteration++]
            );
        }
    }

    function do0To3Callbacks(UnstoppableVault callingContract) public {
        doCallback(callingContract);
        // uint256 functionCount = functionCounts[iteration++];
        // if (functionCount > 3) {
        //     revert BadFunctionCount();
        // }
        // if (functionCount <= 0) {
        //     return;
        // }
        // if (functionCount <= 1) {
        //     doCallback(callingContract);
        // }
        // if (functionCount <= 2) {
        //     doCallback(callingContract);
        // }
        // if (functionCount <= 3) {
        //     doCallback(callingContract);
        // }
    }
}
