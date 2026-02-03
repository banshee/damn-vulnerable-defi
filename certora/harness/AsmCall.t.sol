pragma solidity =0.8.25;

import {Test, console} from "forge-std/Test.sol";
import {AsmCall} from "certora/harness/AsmCall.sol";

contract AsmCallTest is Test {
    AsmCall ac;

    function setUp() public {
        ac = new AsmCall();
    }

    function test_call() public {
        ac.callViaAsm(AsmCall.someMethod.selector);
        assert(ac.v() > 0);
    }
}
