certoraRun = time op run --env-file=$(HOME)/homedir/.env.1password -- mamba run -n certoraweb certoraRun
compile_only = $(certoraRun) --compilation_steps_only
runner_with_options = ${certoraRun} $(common_options)

        # --compilation_steps_only

files = \
        "src/unstoppable/UnstoppableVault.sol" \
        "src/unstoppable/CallbackShim.sol" \
        "src/unstoppable/CallbackNoop.sol" \
        "src/unstoppable/SimpleToken.sol" \
#         "src/unstoppable/SimpleTokenWithCallToSafeTransferFrom.sol" \

common_options = \
        --link UnstoppableVault:asset=SimpleToken \
        --solc solc8.25 \
        --solc_allow_path src \
        --solc_via_ir \
        --optimistic_loop \
        --prover_args '-enableStorageSplitting false' \
        --wait_for_results all \
        --rule_sanity basic

isValidLoan:
	${runner_with_options} $(files) \
        --verify UnstoppableVault:src/unstoppable/certora/isValidLoan.spec \

safeTransferFrom:
	${runner_with_options} $(files) \
        --verify SimpleTokenWithCallToSafeTransferFrom:src/unstoppable/certora/safeTransferFrom.spec \

