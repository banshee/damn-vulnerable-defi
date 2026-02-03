// SPDX-License-Identifier: MIT
// Damn Vulnerable DeFi v4 (https://damnvulnerabledefi.xyz)
pragma solidity =0.8.25;

import {BasicForwarder} from "src/naive-receiver/BasicForwarder.sol";

contract BasicForwarderExecuteWrapper {
    error BadSelector();
    error BadTarget();

    bytes someSignature;

    function executeWrapper(
        BasicForwarder.Request calldata request,
        BasicForwarder basicForwarder,
        bytes4 expectedSelector,
        address expectedTarget
    ) public payable returns (bool success) {
        bytes4 selectorInRequest = bytes4(request.data[:4]);
        if (selectorInRequest != expectedSelector) {
            revert BadSelector();
        }
        if (request.target != expectedTarget) {
            revert BadTarget();
        }
        consoleLog(selectorInRequest, request.target);
        return basicForwarder.execute(request, someSignature);
    }

    uint256 shark;
    function consoleLog(bytes4 b, address a) public {
        shark++;
    }

    function doStuff() public returns (uint256) {
        return 7;
    }
}
