naivefiles = \
	src/naive-receiver/BasicForwarder.sol \
	src/naive-receiver/NaiveReceiverPool.sol \
	src/naive-receiver/FlashLoanReceiver.sol \
	lib/solmate/src/tokens/WETH.sol \

default:
	naive

naive:
	${runner_with_options}  $(naivefiles) \
	--link NaiveReceiverPool:weth=WETH \
	--link NaiveReceiverPool:trustedForwarder=BasicForwarder \
	--multi_assert_check \
	--optimistic_hashing \
	--verify NaiveReceiverPool:$(certoradir)/challenges/naive-receiver/Naive.spec \