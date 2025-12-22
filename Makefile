certoraRun = . ~/.secrets/1passwordtoken.env && time op run --env-file=$(HOME)/homedir/.env.1password -- mamba run -n certoraweb certoraRun
compile_only = $(certoraRun) --compilation_steps_only
runner_with_options = ${certoraRun} $(common_options) $(if $(COMPILE_ONLY),--compilation_steps_only,)

files = \
        "src/unstoppable/UnstoppableVault.sol" \
        "src/unstoppable/certora/harness/UnstoppableVault_Harness.sol" \
        "src/unstoppable/certora/harness/ReentrancyGuardDemo.sol" \
        "src/unstoppable/CallbackNoop.sol" \
        "src/unstoppable/SimpleToken.sol" \

common_options = \
        --link UnstoppableVault:asset=SimpleToken \
        --build_cache \
        --solc solc8.25 \
        --solc_allow_path src \
        --rule_sanity basic \
        --optimistic_loop \
        --prover_args '-enableStorageSplitting false' \
        --wait_for_results all

# x:
# 	${runner_with_options} $(files) \
#         --verify SimpleRe:src/unstoppable/certora/x.spec \

s:
	${runner_with_options} $(files) \
        --verify UnstoppableVault_Harness:src/unstoppable/certora/SoladyReentrantGuard.spec \
        --parametric_contracts UnstoppableVault_Harness
        
rdemo:
	${runner_with_options} $(files) \
        --verify ReentrancyGuardDemo:src/unstoppable/certora/rdemo.spec \
        --parametric_contracts ReentrancyGuardDemo

isValidLoan:
	${runner_with_options} $(files) \
        --rule isValidLoan \
        --verify UnstoppableVault:src/unstoppable/certora/isValidLoan.spec \

safeTransferFrom:
	${runner_with_options} $(files) \
        --verify SimpleTokenWithCallToSafeTransferFrom:src/unstoppable/certora/safeTransferFrom.spec \

