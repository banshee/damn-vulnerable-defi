methods {
        function checkSelectorInCvl(bytes4 aSelector) external returns (bytes4) => checkSelector(aSelector);
}

hook CALL(uint g, address addr, uint value, uint argsOffset, uint argsLength, uint retOffset, uint retLength) uint rc {
}

function checkSelector(bytes4 aSelector) returns (bytes4) {
    require aSelector == to_bytes4(sig:AsmCall.someMethod().selector), "only this selector";
    return aSelector;
}

rule doCall() {
    env e;
    bytes4 someMethodSelector;
    require someMethodSelector == to_bytes4(sig:AsmCall.someMethod().selector), "force selector";
    require currentContract.v == 0, "basic rule";
    currentContract.callViaAsm(e, someMethodSelector);
    assert currentContract.v > 0;
}
