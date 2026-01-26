// ERC20 fields
// owner t_address
// name t_string_storage
// symbol t_string_storage

// totalSupply t_uint256 
//   Changed by mint and burn

// balanceOf t_mapping(t_address,t_uint256)
//   sum of all these must equal the total supply

// allowance t_mapping(t_address,t_mapping(t_address,t_uint256))
// nonces t_mapping(t_address,t_uint256)
// _paused t_bool
// feeRecipient t_address
// loanReceiver t_contract(IERC3156FlashBorrower)39072
