// SPDX-License-Identifier: MIT
pragma solidity ^0.8.25;

contract Bytes4Check {
    error BadSelector();
    error BadTarget();

    struct Request {
        bytes inputData;
    }

    function simpleReturnFromBytes(bytes calldata b) public pure returns (bytes4) {
        return bytes4(b[:4]);
    }

    function simpleReturnFromRequest(Request calldata r) public returns (bytes4) {
        selectorFound = bytes4(r.inputData[:4]);
        return bytes4(selectorFound);
    }

    bytes4 selectorFound;
    bytes4 selectorRequested;

    function matchSelector(
        bytes calldata inputData,
        bytes4 mySelector
    ) public returns (bytes4 result) {
        result = bytes4(inputData[:4]);
        selectorFound = result;
        selectorRequested = mySelector;
        assert(result == mySelector);
        return result;
    }

    bytes4 selectorUsed;
    address targetUsed;

    function matchSelectorInRequest(
        Request calldata request,
        bytes4 mySelector
    ) public returns (bytes4 result) {
        result = bytes4(request.inputData[:4]);
        selectorFound = result;
        selectorUsed = bytes4(request.inputData[:4]);
        // if (selectorUsed != mySelector) {
        //     revert BadSelector();
        // }
        return result;
    }

    function packedSelector(bytes4 mySelector) public pure returns (bytes memory result) {
        return abi.encodePacked(mySelector);
    }

    function buildRequest(bytes4 s) public pure returns (Request memory r) {
        r.inputData = packedSelector(s);
        return r;
    }
}
