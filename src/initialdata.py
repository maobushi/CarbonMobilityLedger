from web3 import Web3
import os
import json

contract_address = "0x7903F0EfF7056fB27F57A35BA6B6bae2DEF87B0a"

infura_url = "https://goerli.infura.io/v3/83987aa77bb741bba949a6e5b1f3ff07"

with open('src/abi/abi.json', 'r') as file:
    contract_abi = json.load(file)

web3 = Web3(Web3.HTTPProvider(infura_url))

contract_object = web3.eth.contract(address=contract_address, abi=contract_abi)
private_key = os.environ.get("METAMASK_DEV_PRIVATE")

