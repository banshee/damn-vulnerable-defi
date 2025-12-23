// SPDX-License-Identifier: MIT

pragma solidity =0.8.25;

import {UnstoppableVault} from "./UnstoppableVault.sol";
import {IERC3156FlashBorrower} from "@openzeppelin/contracts/interfaces/IERC3156.sol";

contract Callback_UnstoppableVault {
    uint256 iteration;
    mapping(uint256 => uint8) functionIds;

    mapping(uint256 => address) parameters_address;

    mapping(uint256 => bool) parameters_bool;

    mapping(uint256 => bytes) parameters_bytes;

    mapping(uint256 => bytes32) parameters_bytes32;

    mapping(uint256 => uint256) parameters_uint256;

    mapping(uint256 => uint8) parameters_uint8;

    function doCallback(
        UnstoppableVault callingContract,
        IERC3156FlashBorrower flashBorrower
    ) public {
        // Note that function count is one greater than the number of functions
        // so this function can be a noop
        uint8 functionId = functionIds[iteration++] % 14;

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
        } else if (functionId == 2) {
            callingContract.execute(
                parameters_address[iteration++],
                parameters_bytes[iteration++]
            );
        } else if (functionId == 3) {
            callingContract.flashLoan(
                flashBorrower,
                parameters_address[iteration++],
                parameters_uint256[iteration++],
                parameters_bytes[iteration++]
            );
        } else if (functionId == 4) {
            callingContract.mint(
                parameters_uint256[iteration++],
                parameters_address[iteration++]
            );
        } else if (functionId == 5) {
            callingContract.permit(
                parameters_address[iteration++],
                parameters_address[iteration++],
                parameters_uint256[iteration++],
                parameters_uint256[iteration++],
                parameters_uint8[iteration++],
                parameters_bytes32[iteration++],
                parameters_bytes32[iteration++]
            );
        } else if (functionId == 6) {
            callingContract.redeem(
                parameters_uint256[iteration++],
                parameters_address[iteration++],
                parameters_address[iteration++]
            );
        } else if (functionId == 7) {
            callingContract.setFeeRecipient(parameters_address[iteration++]);
        } else if (functionId == 8) {
            callingContract.setPause(parameters_bool[iteration++]);
        } else if (functionId == 9) {
            callingContract.transfer(
                parameters_address[iteration++],
                parameters_uint256[iteration++]
            );
        } else if (functionId == 10) {
            callingContract.transferFrom(
                parameters_address[iteration++],
                parameters_address[iteration++],
                parameters_uint256[iteration++]
            );
        } else if (functionId == 11) {
            callingContract.transferOwnership(parameters_address[iteration++]);
        } else if (functionId == 12) {
            callingContract.withdraw(
                parameters_uint256[iteration++],
                parameters_address[iteration++],
                parameters_address[iteration++]
            );
        }
    }

    function do2Callbacks(UnstoppableVault callingContract, IERC3156FlashBorrower flashBorrower) public {
        doCallback(callingContract, flashBorrower);
        doCallback(callingContract, flashBorrower);
    }
}
