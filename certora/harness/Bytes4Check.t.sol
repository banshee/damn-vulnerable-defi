// SPDX-License-Identifier: MIT
// Damn Vulnerable DeFi v4 (https://damnvulnerabledefi.xyz)
pragma solidity =0.8.25;

import {Test, console} from "forge-std/Test.sol";
import {BasicForwarderExecuteWrapper} from "certora/challenges/naive-receiver/harness/BasicForwarderExecuteWrapper.sol";
import {BasicForwarder} from "src/naive-receiver/BasicForwarder.sol";

contract Bytes4Check is Test {
    Bytes4Check check;

    function setUp() public {
        check = new Bytes4Check();
    }

    function test_stuff() public {
        bytes4 mySelector = BasicForwarder.basicStuff.selector;

        BasicForwarder.Request memory request;
        request.data = abi.encodePacked(mySelector);
        request.target = address(basic);
        request.gas = 10 ether;

        bool result = wrapper.executeWrapper(request, basic, mySelector, address(basic));

        assertTrue(result);
    }
}
