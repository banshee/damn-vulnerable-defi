rule extract4Bytes() {
    env e;
    bytes4 feedFace = to_bytes4(0xfeedface);
    bytes testBytes = currentContract.bytes4ToBytes(e, feedFace);
    bytes4 result = currentContract.extract4Bytes(e, testBytes);
    assert result == feedFace;
}

rule extract4BytesFromRequest() {
    env e;
    bytes4 feedFace = to_bytes4(0xfeedface);
    Bytes4Check.Request r = currentContract.bytes4ToRequestWithBytesField(e, feedFace);
    bytes4 result = currentContract.extract4BytesFromRequest(e, r);
    assert result == feedFace;
}