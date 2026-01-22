certoradir = src/unstoppable/certora
certoraRun = . ~/.secrets/1passwordtoken.env && time op run --env-file=$(HOME)/homedir/.env.1password -- mamba run -n certora certoraRun
compile_only = $(certoraRun) --compilation_steps_only
runner_with_options = ${certoraRun} $(common_options) $(if $(COMPILE_ONLY),--compilation_steps_only,)

files = \
        "src/DamnValuableToken.sol" \
        "src/unstoppable/UnstoppableVault.sol" \
        "src/unstoppable/certora/harness/SimpleFlashReceiver.sol" \

common_options = \
        --link UnstoppableVault:asset=DamnValuableToken \
        --auto_dispatcher \
        --solc solc8.25 \
        --solc_allow_path src \
        --rule_sanity basic \
        --optimistic_loop \
        --contract_recursion_limit 2 \

.PHONY: isValidLoan

isValidLoan:
	${runner_with_options} $(files) \
        --verify UnstoppableVault:$(certoradir)/spec/isValidLoan.spec \
        --parametric_contracts UnstoppableVault DamnValuableToken \

break:
	${runner_with_options} $(files) \
        --verify UnstoppableVault_Harness:$(certoradir)/spec/breakTheContract.spec \
        --parametric_contracts UnstoppableVault_Harness \

st:
	${runner_with_options} $(files) \
	--link UnstoppableVault_Harness:loanReceiver=CallbackNoop \
        --parametric_contracts SimpleToken \
        --verify SimpleToken:$(certoradir)/spec/SimpleToken.spec \

x:
	${runner_with_options} $(files) \
	--link UnstoppableVault_Harness:loanReceiver=CallbackNoop \
        --parametric_contracts UnstoppableVault_Harness \
        --verify UnstoppableVault_Harness:$(certoradir)/spec/UnstoppableVaultAsToken.spec \

