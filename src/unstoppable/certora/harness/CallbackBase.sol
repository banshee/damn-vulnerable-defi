// SPDX-License-Identifier: MIT
// Damn Vulnerable DeFi v4 (https://damnvulnerabledefi.xyz)
pragma solidity =0.8.25;

import {IERC3156FlashBorrower} from "@openzeppelin/contracts/interfaces/IERC3156.sol";
import {UnstoppableVault} from "src/unstoppable/UnstoppableVault.sol";
import {ERC20} from "@openzeppelin/contracts/token/ERC20/ERC20.sol";

/**
 * An ERC4626-compliant tokenized vault offering flashloans for a fee.
 * An owner can pause the contract and execute arbitrary changes.
 */
contract CallbackBase is IERC3156FlashBorrower {
    bytes32 public constant RETURN_VALUE =
        keccak256("IERC3156FlashBorrower.onFlashLoan");

    UnstoppableVault public targetVault;

    uint256 public loanFee;

    uint256 public balanceDuringLoan;

    bool public executeCallbacks;

    uint256 public functionId;

    error NotEnoughBalance();

    function executePossibleCallbacks() internal virtual returns (uint256) {
        return 0;
    }

    function onFlashLoan(
        address initiator,
        address token,
        uint256 amount,
        uint256 fee,
        bytes calldata data
    ) external virtual returns (bytes32) {
        loanFee = fee;
        balanceDuringLoan = ERC20(token).balanceOf(address(this));
        if (balanceDuringLoan < amount + fee) {
            revert NotEnoughBalance();
        }
        if (executeCallbacks) {
            functionId = executePossibleCallbacks();
        }
        ERC20(token).approve(msg.sender, amount + fee);
        return RETURN_VALUE;
    }
}
