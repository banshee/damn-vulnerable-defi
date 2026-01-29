// SPDX-License-Identifier: MIT
// Damn Vulnerable DeFi v4 (https://damnvulnerabledefi.xyz)
pragma solidity =0.8.25;

import {Test, console} from "forge-std/Test.sol";
import {BasicForwarderExecuteWrapper} from "certora/challenges/naive-receiver/harness/BasicForwarderExecuteWrapper.sol";
import {BasicForwarder} from "src/naive-receiver/BasicForwarder.sol";

contract BasicForwarderExecuteWrapperTest is Test {
    address deployer = makeAddr("deployer");
    address recovery = makeAddr("recovery");
    address player;
    uint256 playerPk;

    uint256 constant WETH_IN_POOL = 1000e18;
    uint256 constant WETH_IN_RECEIVER = 10e18;

    BasicForwarderExecuteWrapper wrapper;
    BasicForwarder basic;

    function setUp() public {
        (player, playerPk) = makeAddrAndKey("player");
        startHoax(deployer);

        // Deploy forwarder
        wrapper = new BasicForwarderExecuteWrapper();
        basic = new BasicForwarder();
    }

    function test_stuff() public {
        // struct Request {
        //     address from;
        //     address target;
        //     uint256 value;
        //     uint256 gas;
        //     uint256 nonce;
        //     bytes data;
        //     uint256 deadline;
        // }

        bytes4 mySelector = BasicForwarder.basicStuff.selector;

        BasicForwarder.Request memory request;
        request.data = abi.encodePacked(mySelector);
        request.target = address(basic);
        request.gas = 10 ether;

        bool result = wrapper.executeWrapper(request, basic, mySelector, address(basic));

        assertTrue(result);
    }
}
