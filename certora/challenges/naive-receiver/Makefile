files = \
	src/naive-receiver/BasicForwarder.sol \
	src/naive-receiver/NaiveReceiverPool.sol \
	src/naive-receiver/FlashLoanReceiver.sol \
	lib/solmate/src/tokens/WETH.sol \
	certora/challenges/naive-receiver/harness/BasicForwarderExecuteWrapper.sol

default:
	naive

naive:
	${runner_with_options}  $(files) \
	--link NaiveReceiverPool:weth=WETH \
	--link NaiveReceiverPool:trustedForwarder=BasicForwarder \
	--link NaiveReceiverPool:feeReceiver=FlashLoanReceiver \
	--optimistic_hashing \
	--verify NaiveReceiverPool:$(certoradir)/challenges/naive-receiver/Naive.spec \
#     --parametric_contracts WETH BasicForwarder FlashLoanReceiver NaiveReceiverPool BasicForwarderExecuteWrapper