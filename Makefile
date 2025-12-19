certoraRun = . ~/.secrets/1passwordtoken.env && time op run --env-file=$(HOME)/homedir/.env.1password -- mamba run -n certoraweb certoraRun
compile_only = $(certoraRun) --compilation_steps_only
runner_with_options = ${certoraRun} $(common_options) $(if $(COMPILE_ONLY),--compilation_steps_only,)

files = \
        "src/unstoppable/UnstoppableVault.sol" \
        "src/unstoppable/CallbackNoop.sol" \
        "src/unstoppable/SimpleToken.sol" \

common_options = \
        --link UnstoppableVault:asset=SimpleToken \
        --solc solc8.25 \
        --solc_allow_path src \
        --rule isValidLoan \
        --rule_sanity basic \
#         --wait_for_results all \

isValidLoan:
	${runner_with_options} $(files) \
        --verify UnstoppableVault:src/unstoppable/certora/isValidLoan.spec \

safeTransferFrom:
	${runner_with_options} $(files) \
        --verify SimpleTokenWithCallToSafeTransferFrom:src/unstoppable/certora/safeTransferFrom.spec \

