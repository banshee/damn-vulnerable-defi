files = \
	src/naive-receiver/BasicForwarder.sol \
	src/naive-receiver/NaiveReceiverPool.sol \
	src/naive-receiver/FlashLoanReceiver.sol \
	lib/solmate/src/tokens/WETH.sol \

default:
	naive

naive:
	${runner_with_options}  $(files) \
	--link NaiveReceiverPool:weth=WETH \
	--link NaiveReceiverPool:trustedForwarder=BasicForwarder \
	--link NaiveReceiverPool:feeReceiver=FlashLoanReceiver \
	--verify NaiveReceiverPool:$(certoradir)/challenges/naive-receiver/Naive.spec \
        --parametric_contracts WETH BasicForwarder FlashLoanReceiver