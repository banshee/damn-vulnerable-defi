// SPDX-License-Identifier: MIT
pragma solidity ^0.8.25;

contract Tiny {
    uint256 codesizeInConstructor;
    uint256 codesizeInMethod;
    uint256 extCodesizeInConstructor;
    uint256 extCodesizeInMethod;

    constructor() {
        address x = address(this);
        assembly {
            sstore(codesizeInConstructor.slot, codesize())
            sstore(extCodesizeInConstructor.slot, extcodesize(x))
        }
    }

    function setCodesize() public {
        address x = address(this);
        assembly {
            sstore(codesizeInMethod.slot, codesize())
            sstore(extCodesizeInMethod.slot, extcodesize(x))
        }
    }

    function returnCodesize() public pure returns (uint256 s) {
        assembly {
            s := codesize()
        }
    }
}
