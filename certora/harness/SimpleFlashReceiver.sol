// SPDX-License-Identifier: Apache-2.0

pragma solidity =0.8.25;

import {ERC20} from "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import {IERC3156FlashBorrower} from "@openzeppelin/contracts/interfaces/IERC3156.sol";

contract SimpleFlashReceiver is IERC3156FlashBorrower {
    bytes32 public constant RETURN_VALUE =
        keccak256("IERC3156FlashBorrower.onFlashLoan");

    error NotEnoughBalance();

    function onFlashLoan(
        address initiator,
        address token,
        uint256 amount,
        uint256 fee,
        bytes calldata data
    ) external virtual returns (bytes32) {
        uint256 balanceDuringLoan = ERC20(token).balanceOf(address(this));
        if (balanceDuringLoan < amount + fee) {
            revert NotEnoughBalance();
        }
        ERC20(token).approve(msg.sender, amount + fee);
        return RETURN_VALUE;
    }
}
