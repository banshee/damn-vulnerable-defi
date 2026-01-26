function notZero3(address a, address b, address c) returns (bool) {
    return a != 0 && b != 0 && c != 0;
}

function notEqual3(address a, address b, address c) returns (bool) {
    return a != b && a != c && b != c;
}

function notEqualAndNotZero3(address a, address b, address c) returns (bool) {
    return notEqual3(a, b, c) && notZero3(a, b, c);
}

function notZero4(address a, address b, address c, address d) returns bool {
    return a != 0 && b != 0 && c != 0 && d != 0;
}

function notEqual4(address a, address b, address c, address d) returns bool {
    return a != b && a != c && a != d 
        && b != c && b != d 
        && c != d;
}

function notEqualAndNotZero4(address a, address b, address c, address d) returns bool {
    return notEqual4(a, b, c, d) && notZero4(a, b, c, d);
}

function notZero5(address a, address b, address c, address d, address e) returns bool {
    return a != 0 && b != 0 && c != 0 && d != 0 && e != 0;
}

function notEqual5(address a, address b, address c, address d, address e) returns bool {
    return a != b && a != c && a != d && a != e
        && b != c && b != d && b != e
        && c != d && c != e
        && d != e;
}

function notEqualAndNotZero5(address a, address b, address c, address d, address e) returns bool {
    return notEqual5(a, b, c, d, e) && notZero5(a, b, c, d, e);
}

function notZero6(address a, address b, address c, address d, address e, address f) returns (bool) {
    return a != 0 && b != 0 && c != 0 && d != 0 && e != 0 && f != 0;
}

function notEqual6(address a, address b, address c, address d, address e, address f) returns (bool) {
    return a != b && a != c && a != d && a != e && a != f
        && b != c && b != d && b != e && b != f
        && c != d && c != e && c != f
        && d != e && d != f
        && e != f;
}

function notEqualAndNotZero6(address a, address b, address c, address d, address e, address f) returns (bool) {
    return notEqual6(a, b, c, d, e, f) && notZero6(a, b, c, d, e, f);
}