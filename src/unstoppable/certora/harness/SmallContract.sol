// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

contract SmallContract {
    uint256 public v1;
    uint256 public v2;

    constructor() {
        v1 = gs();
        v2 = gs();
    }

    function getCodesize() public pure returns (uint256 s) {
        return gs();
    }

    function gs() internal pure returns (uint256 s) {
        assembly {
            s := codesize()
        }
    }

    function updateVX() external returns (bool) {
        v1 = gs();
        v2 = gs();
        return true;
    }

    function doNothing() external returns (bool) {
        // The function name is a lie!
        v2 = v1 + 1;
        return true;
    }
}
