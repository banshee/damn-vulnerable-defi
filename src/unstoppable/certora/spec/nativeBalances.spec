function isZeroNativeBalance2(address a, address b) returns (bool) {
    return nativeBalances[a] == 0 && nativeBalances[b] == 0;
}

function isZeroNativeBalance3(address a, address b, address c) returns bool {
    return nativeBalances[a] == 0 && nativeBalances[b] == 0 && nativeBalances[c] == 0;
}

function isZeroNativeBalance4(address a, address b, address c, address d) returns bool {
    return nativeBalances[a] == 0 && nativeBalances[b] == 0 && nativeBalances[c] == 0 && nativeBalances[d] == 0;
}

function isZeroNativeBalance5(address a, address b, address c, address d, address e) returns bool {
    return nativeBalances[a] == 0 && nativeBalances[b] == 0 && nativeBalances[c] == 0 && nativeBalances[d] == 0 && nativeBalances[e] == 0;
}
