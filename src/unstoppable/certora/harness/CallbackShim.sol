// SPDX-License-Identifier: MIT
// Damn Vulnerable DeFi v4 (https://damnvulnerabledefi.xyz)
pragma solidity =0.8.25;

import {IERC3156FlashBorrower} from "@openzeppelin/contracts/interfaces/IERC3156.sol";
import {UnstoppableVault} from "../../UnstoppableVault.sol";
import {ERC20} from "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import {Callback_UnstoppableVault} from "./Callback_UnstoppableVault.sol";


/**
 * An ERC4626-compliant tokenized vault offering flashloans for a fee.
 * An owner can pause the contract and execute arbitrary changes.
 */
contract CallbackShim is IERC3156FlashBorrower, Callback_UnstoppableVault {
    bytes32 public constant RETURN_VALUE =
        keccak256("IERC3156FlashBorrower.onFlashLoan");

    uint256 public loanFee;

    error NotEnoughBalance();

    address public targetVault;

    function onFlashLoan(
        address initiator,
        address token,
        uint256 amount,
        uint256 fee,
        bytes calldata data
    ) external returns (bytes32) {
        loanFee = fee;
        if (ERC20(token).balanceOf(address(this)) < amount + fee) {
            revert NotEnoughBalance();
        }
        ERC20(token).approve(msg.sender, amount + fee);
        return RETURN_VALUE;
    }
}
