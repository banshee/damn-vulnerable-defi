pragma solidity =0.8.25;

import {Test, console} from "forge-std/Test.sol";
import {Bytes4Check} from "certora/harness/Bytes4Check.sol";

contract Bytes4CheckTest is Test {
    Bytes4Check bytes4Check;

    function setUp() public {
        bytes4Check = new Bytes4Check();
    }

    function test_extract4Bytes() public {
        bytes memory testBytes = bytes4Check.bytes4ToBytes(0xfeedface);

        bytes4 result = bytes4Check.extract4Bytes(testBytes);

        assertTrue(result == 0xfeedface);
    }

    function test_extract4BytesFromRequest() public {
        Bytes4Check.Request memory request = bytes4Check
            .bytes4ToRequestWithBytesField(0xfeedface);
        bytes4 result = bytes4Check.extract4BytesFromRequest(request);

        assertTrue(result == 0xfeedface);
    }
}
