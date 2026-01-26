methods {
    function _.balanceOf(address) external envfree;
}

function isZeroTokenBalance2(address token, address a, address b) returns (bool) {
    return token.balanceOf(a) == 0 && IERC20(token).balanceOf(b) == 0;
}

function isZeroTokenBalance3(address token, address a, address b, address c) returns (bool) {
    return token.balanceOf(a) == 0 
        && token.balanceOf(b) == 0 
        && token.balanceOf(c) == 0
        && token.balanceOf(c) == 0;
}

function isZeroTokenBalance4(address token, address a, address b, address c, address d) returns (bool) {
    return token.balanceOf(a) == 0 
        && token.balanceOf(b) == 0 
        && token.balanceOf(c) == 0 
        && token.balanceOf(d) == 0;
}

function isZeroTokenBalance5(address token, address a, address b, address c, address d, address e) returns (bool) {
    return token.balanceOf(a) == 0 
        && token.balanceOf(b) == 0 
        && token.balanceOf(c) == 0 
        && token.balanceOf(d) == 0 
        && token.balanceOf(e) == 0;
}