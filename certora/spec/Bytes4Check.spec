rule matchSelector() {
    bytes inputData;
    bytes4 mySelector = to_bytes4(0xcafebeef);
    env e;
    bytes4 result = matchSelector(e, inputData, mySelector);
    assert result == mySelector;
}

rule matchSelectorInRequest() {
    bytes4 mySelector = to_bytes4(0xcafebeef);
    env e;
    Bytes4Check.Request r = buildRequest(e, mySelector);
    bytes4 result = matchSelectorInRequest(e, r, mySelector);
    assert result == mySelector;
    assert mySelector == currentContract.selectorFound;
}

rule checkBytes4() {
    bytes4 mySelector = to_bytes4(0xcafebeef);
    env e;
    bytes b = packedSelector(e, mySelector);
    bytes4 result = simpleReturnFromBytes(e, b);
    assert result == mySelector;
}

rule checkBytes4UsingStruct() {
    bytes4 mySelector = to_bytes4(0xcafebeef);
    env e;
    Bytes4Check.Request r = buildRequest(e, mySelector);
    bytes4 result = simpleReturnFromRequest(e, r);
    assert currentContract.selectorFound == mySelector;
    assert result == mySelector;
}