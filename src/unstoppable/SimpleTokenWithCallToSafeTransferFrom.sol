// SPDX-License-Identifier: MIT
// Damn Vulnerable DeFi v4 (https://damnvulnerabledefi.xyz)
pragma solidity =0.8.25;

import {SafeTransferLib, ERC20} from "solmate/tokens/ERC4626.sol";

contract SimpleTokenWithCallToSafeTransferFrom is ERC20 {
    constructor() ERC20("Simple Token", "STKN", 18) {
        _mint(msg.sender, 1_000_000 ether);
    }

    function reproSafeTransferFromHavoc(address from, address to, uint256 amount) public {
        SafeTransferLib.safeTransferFrom(ERC20(this), from, to, amount);
    }
}
