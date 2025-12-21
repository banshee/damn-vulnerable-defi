// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

/// Hacked version of Solady, just to demo a problem:
/// @notice Reentrancy guard mixin.
/// @author Solady (https://github.com/vectorized/solady/blob/main/src/utils/ReentrancyGuard.sol)

// guard value is either contract codesize (unlocked) or contract address (locked), or zero (uninitialized)
contract ReentrancyGuardDemo {
    event EnterNonReentrant(address thisContract, uint256 startingValue);
    event ExitNonReentrant(address thisContract, uint256 startingValue, uint256 endingValue);

    uint256 public guardValueInsideCall;

    /*´:°•.°+.*•´.*:˚.°*.˚•´.°:°•.°•.*•´.*:˚.°*.˚•´.°:°•.°+.*•´.*:*/
    /*                       CUSTOM ERRORS                        */
    /*.•°:°.´+˚.*°.˚:*.´•*.+°.•°:´*.´•*.•°.•°:°.´:•˚°.*°.˚:*.´+°.•*/

    /// @dev Unauthorized reentrant call.
    error Reentrancy();

    /*´:°•.°+.*•´.*:˚.°*.˚•´.°:°•.°•.*•´.*:˚.°*.˚•´.°:°•.°+.*•´.*:*/
    /*                          STORAGE                           */
    /*.•°:°.´+˚.*°.˚:*.´•*.+°.•°:´*.´•*.•°.•°:°.´:•˚°.*°.˚:*.´+°.•*/

    /// @dev Equivalent to: `uint72(bytes9(keccak256("_REENTRANCY_GUARD_SLOT")))`.
    /// 9 bytes is large enough to avoid collisions with lower slots,
    /// but not too large to result in excessive bytecode bloat.
    uint256 private constant _REENTRANCY_GUARD_SLOT = 0x929eee149b4bd21268;

    /*´:°•.°+.*•´.*:˚.°*.˚•´.°:°•.°•.*•´.*:˚.°*.˚•´.°:°•.°+.*•´.*:*/
    /*                      REENTRANCY GUARD                      */
    /*.•°:°.´+˚.*°.˚:*.´•*.+°.•°:´*.´•*.•°.•°:°.´:•˚°.*°.˚:*.´+°.•*/

    /// @dev Guards a function from reentrancy.
    modifier nonReentrant() virtual {
        /// @solidity memory-safe-assembly
        assembly {
            if eq(sload(_REENTRANCY_GUARD_SLOT), codesize()) {
                mstore(0x00, 0xab143c06) // `Reentrancy()`.
                revert(0x1c, 0x04)
            }
            sstore(_REENTRANCY_GUARD_SLOT, address())
        }
        uint256 startingValue;
        assembly {
            startingValue := sload(_REENTRANCY_GUARD_SLOT)
        }
        emit EnterNonReentrant(address(this), startingValue);
        _;
        /// @solidity memory-safe-assembly
        uint256 endingValue;
        assembly {
            sstore(_REENTRANCY_GUARD_SLOT, codesize())
            endingValue := sload(_REENTRANCY_GUARD_SLOT)
        }
        emit ExitNonReentrant(address(this), startingValue, endingValue);
    }

    /// @dev Returns the raw value stored in the guard slot.
    /// Unlocked = contract codesize
    /// Locked = contract address
    function getReentrancyGuardValue() external view returns (uint256 status) {
        assembly {
            status := sload(_REENTRANCY_GUARD_SLOT)
        }
    }

    /// @dev Helper to return a boolean indicating if the contract is currently locked.
    function isLocked() public view returns (bool) {
        // Solady sets the slot to address(this) when locked.
        return this.getReentrancyGuardValue() == uint256(uint160(address(this)));
    }

    function shark() external nonReentrant returns (bool){
        guardValueInsideCall = this.getReentrancyGuardValue();
        return true;
    }

    function getCodesize() public pure returns (uint256 s) {
        assembly {
            s := codesize()
        }
    }
}
