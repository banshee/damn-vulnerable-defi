run = mamba run -n certoraweb
compile_only = ${run} --compilation_steps_only

files = 
        "src/unstoppable/UnstoppableVault.sol" \
        "src/unstoppable/CallbackShim.sol" \
        "src/unstoppable/CallbackNoop.sol" \
        "src/unstoppable/SimpleToken.sol" \

common_options = \

#     "verify": "UnstoppableVault:src/unstoppable/certora/UnstoppableVaultCanRepeat.spec",
#     "link": [
#         "UnstoppableVault:asset=SimpleToken"
#     ],
#     "wait_for_results": "all",
#     "rule_sanity": "basic",
#     "solc": "solc8.25",
#     "solc_allow_path": "src",
#     "solc_via_ir": true,
#     "optimistic_loop": true,
#     "prover_args": '-enableStorageSplitting false'
# }

isValidLoan:
	${compile_only} $files --verify certora/isValidLoanRule.spec