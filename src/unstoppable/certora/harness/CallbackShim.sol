// SPDX-License-Identifier: MIT
// Damn Vulnerable DeFi v4 (https://damnvulnerabledefi.xyz)
pragma solidity =0.8.25;

import {IERC3156FlashBorrower} from "@openzeppelin/contracts/interfaces/IERC3156.sol";
import {Callback_UnstoppableVault} from "./Callback_UnstoppableVault.sol";
import {CallbackNoop} from "./CallbackNoop.sol";
import {UnstoppableVault} from "src/unstoppable/UnstoppableVault.sol";
import {ERC20} from "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract CallbackShim is IERC3156FlashBorrower, Callback_UnstoppableVault {
    bytes32 public constant RETURN_VALUE =
        keccak256("IERC3156FlashBorrower.onFlashLoan");

    UnstoppableVault public immutable targetVault;

    function onFlashLoan(
        address initiator,
        address token,
        uint256 amount,
        uint256 fee,
        bytes calldata data
    ) external override returns (bytes32) {
        doCallback(targetVault, this);
        ERC20(token).approve(msg.sender, amount + fee);
        return RETURN_VALUE;
    }
}
