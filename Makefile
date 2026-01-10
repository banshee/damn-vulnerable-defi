certoradir = src/unstoppable/certora
certoraRun = . ~/.secrets/1passwordtoken.env && time op run --env-file=$(HOME)/homedir/.env.1password -- mamba run -n certora certoraRun
compile_only = $(certoraRun) --compilation_steps_only
runner_with_options = ${certoraRun} $(common_options) $(if $(COMPILE_ONLY),--compilation_steps_only,)

files = \
        "src/unstoppable/certora/harness/UnstoppableVault_Harness.sol" \
        "src/unstoppable/certora/harness/ReentrancyGuardDemo.sol" \
        "src/unstoppable/certora/harness/CallbackNoop.sol" \
        "src/unstoppable/certora/harness/CallbackShim.sol" \
        "src/unstoppable/certora/harness/CallbackBase.sol" \
        "src/unstoppable/SimpleToken.sol" \

common_options = \
        --link UnstoppableVault_Harness:asset=SimpleToken \
        --link CallbackShim:targetVault=UnstoppableVault_Harness \
        --build_cache \
        --solc solc8.25 \
        --solc_allow_path src \
        --rule_sanity basic \
        --optimistic_loop \
        --prover_args '-enableStorageSplitting false' \
        --wait_for_results all \
        --contract_recursion_limit 2 \

.PHONY: isValidLoan isValidLoanCB s SoladyReentrantGuard

baseIsValidLoanOptions = \
	${runner_with_options} $(files) \
        --verify UnstoppableVault_Harness:$(certoradir)/spec/isValidLoan.spec \
        --parametric_contracts UnstoppableVault_Harness \

isValidLoanCB:
	${baseIsValidLoanOptions} \
	--link UnstoppableVault_Harness:loanReceiver=CallbackShim \
        --rule isValidSubsequentLoan \

isValidLoan:
	${baseIsValidLoanOptions} \
	--link UnstoppableVault_Harness:loanReceiver=CallbackNoop \
        --rule goodBalances \

st:
	${runner_with_options} $(files) \
	--link UnstoppableVault_Harness:loanReceiver=CallbackNoop \
        --parametric_contracts SimpleToken \
        --verify SimpleToken:$(certoradir)/spec/SimpleToken.spec \

x:
	${runner_with_options} $(files) \
        --verify UnstoppableVault_Harness:$(certoradir)/spec/x.spec \
        --parametric_contracts UnstoppableVault_Harness \
        --rule x \

