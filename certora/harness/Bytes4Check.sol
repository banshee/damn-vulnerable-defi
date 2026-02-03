// SPDX-License-Identifier: MIT
pragma solidity ^0.8.25;

contract Bytes4Check {
    struct Request {
        bytes bytesField;
    }

    bytes4 extractedBytes;

    function extract4Bytes(bytes calldata b) public returns (bytes4) {
        extractedBytes = bytes4(b[:4]);
        justUsedToGetTheUiToShowAField(extractedBytes);
        return bytes4(b[:4]);
    }

    function extract4BytesFromRequest(
        Request calldata r
    ) public returns (bytes4) {
        extractedBytes = bytes4(r.bytesField[:4]);
        justUsedToGetTheUiToShowAField(extractedBytes);
        return bytes4(extractedBytes);
    }

    function bytes4ToBytes(bytes4 b) public returns (bytes memory result) {
        return abi.encodePacked(b);
    }

    function bytes4ToRequestWithBytesField(bytes4 b) public returns (Request memory r) {
        r.bytesField = abi.encodePacked(b);
        return r;
    }

    uint32 bogusField;

    function justUsedToGetTheUiToShowAField(bytes4 b) public returns (bytes4) {
        bogusField += 1;
        return b;
    }
}