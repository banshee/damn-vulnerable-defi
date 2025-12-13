// This hook + ghost combination lets you see all SLOADs done by the contract under analysis.
// Very useful to see what storage slots are being read.
// This is a tool for understanding what's happening, not a specific property to verify.

ghost mapping(address => mapping(uint => uint)) ghostSLoad {
    init_state axiom forall address _executingContract. forall uint _slot. ghostSLoad[_executingContract][_slot] == 0;
}

// Reminder: executingContract is a built-in variable that points to the contract being analyzed
hook ALL_SLOAD(uint slot) uint val {
    ghostSLoad[executingContract][slot] = val;
}
