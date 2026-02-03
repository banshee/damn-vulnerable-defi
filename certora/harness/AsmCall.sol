// SPDX-License-Identifier: MIT
pragma solidity ^0.8.25;

contract AsmCall {
    uint256 public v;

    function someMethod() public returns (bool) {
        v++;
        return true;
    }

    // This exists only to be overridden by CVL
    function checkSelectorInCvl(bytes4 aSelector) public pure returns (bytes4) {
        return aSelector;
    }

    function callViaAsm(bytes4 aSelector) public returns (bool success) {
        bytes4 s = checkSelectorInCvl(aSelector);
        bytes memory payload = abi.encodeWithSelector(s);
        assembly {
            success := call(
                gas(),
                address(),
                0,
                add(payload, 0x20),
                mload(payload),
                0,
                0
            )
        }
    }
}
