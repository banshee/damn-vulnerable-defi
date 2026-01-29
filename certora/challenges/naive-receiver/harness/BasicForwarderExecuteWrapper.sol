// SPDX-License-Identifier: MIT
// Damn Vulnerable DeFi v4 (https://damnvulnerabledefi.xyz)
pragma solidity =0.8.25;

import {BasicForwarder} from "src/naive-receiver/BasicForwarder.sol";

contract BasicForwarderExecuteWrapper {
    error BadSelector();
    error BadTarget();

    uint256 someField;

    bytes4 selectorUsed;
    address targetUsed;

    bytes someSignature;

    function executeWrapper(
        BasicForwarder.Request calldata request,
        BasicForwarder basicForwarder,
        bytes4 expectedSelector,
        address expectedTarget
    ) public payable returns (bool success) {
        selectorUsed = bytes4(request.data[:4]);
        targetUsed = request.target;
        if (selectorUsed != expectedSelector) {
            revert BadSelector();
        }
        if (request.target != expectedTarget) {
            revert BadTarget();
        }
        return basicForwarder.execute(request, someSignature);
    }

    function doStuff() public returns (uint256) {
        someField += 1;
        return someField;
    }
}
