certoradir = src/unstoppable/certora
certoraRun = . ~/.secrets/1passwordtoken.env && time op run --env-file=$(HOME)/homedir/.env.1password -- mamba run -n certoraweb certoraRun
compile_only = $(certoraRun) --compilation_steps_only
runner_with_options = ${certoraRun} $(common_options) $(if $(COMPILE_ONLY),--compilation_steps_only,)

files = \
        "src/unstoppable/UnstoppableVault.sol" \
        "src/unstoppable/certora/harness/UnstoppableVault_Harness.sol" \
        "src/unstoppable/certora/harness/ReentrancyGuardDemo.sol" \
        "src/unstoppable/certora/harness/CallbackNoop.sol" \
        "src/unstoppable/certora/harness/CallbackShim.sol" \
        "src/unstoppable/SimpleToken.sol" \

common_options = \
        --link UnstoppableVault:asset=SimpleToken \
        --link UnstoppableVault_Harness:asset=SimpleToken \
        --link CallbackShim:targetVault=UnstoppableVault_Harness \
        --build_cache \
        --solc solc8.25 \
        --solc_allow_path src \
        --rule_sanity basic \
        --optimistic_loop \
        --prover_args '-enableStorageSplitting false' \
        --wait_for_results all

baseIsValidLoanOptions = \
	${runner_with_options} $(files) \
        --verify UnstoppableVault_Harness:$(certoradir)/spec/isValidLoan.spec \
        --parametric_contracts UnstoppableVault_Harness \

.PHONY: isValidLoan isValidLoanCB

isValidLoanCB:
	${baseIsValidLoanOptions} \
	--link UnstoppableVault_Harness:loanReceiver=CallbackShim \

isValidLoan:
	${baseIsValidLoanOptions} \
	--link UnstoppableVault_Harness:loanReceiver=CallbackNoop \

s SoladyReentrantGuard:
	${runner_with_options} $(files) \
        --verify UnstoppableVault_Harness:src/unstoppable/certora/SoladyReentrantGuard.spec \
        --parametric_contracts UnstoppableVault_Harness
