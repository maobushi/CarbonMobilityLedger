import streamlit as st
from wallet_connect import wallet_connect
from streamlit_option_menu import option_menu
import time
import streamlit as st
from web3 import Web3
import os

from initialdata import contract_address, contract_abi,  contract_object , private_key, infura_url, web3
from web3.exceptions import TransactionNotFound

import streamlit as st
from web3 import Web3
# 他のインポート...

def plant_page():
	user_wallet_address = st.session_state.user_wallet_address
	st.title('Plant a Tree with CBT')
	#amount_to_burn_wei = amount * 1e18  # Convert CBT to Wei

	# ユーザーのCBT残高を取得し、Ether単位に変換
	cbt_balance_wei = contract_object.functions.balanceOf(user_wallet_address).call()
	cbt_balance = web3.from_wei(cbt_balance_wei, 'ether')  # WeiからEtherへの変換

	# 1,000,000 CBTごとに1本植えられる計算
	max_trees = int(cbt_balance / 10**16)  # 1_000_000で割って整数に変換
	max_trees = max_trees // 1000
	# 植える木の量をスライダーで入力
	amount = st.slider('Amount of trees to plant (1 tree per 1,000,000 CBT)', 
					min_value=0, 
					max_value=max_trees, 
					step=1)

	# 植樹を実行するボタン
	if st.button('Plant Trees'):
		if amount > 0:
			carbon_token_wei = int(amount * 1000 * 1e18)  # 修正された計算
			user_wallet_address = st.session_state.user_wallet_address
			nonce = web3.eth.get_transaction_count(user_wallet_address)

			transaction = contract_object.functions.plantTree(carbon_token_wei).build_transaction({
				'chainId': 5,
				'gas': 2000000,
				'gasPrice': web3.to_wei('50', 'gwei'),
				'from': user_wallet_address,
				'nonce': nonce
			})
			st.write("使用したCBT量: ", carbon_token_wei)
			# ここでトランザクションを署名する
			private_key = os.environ['METAMASK_DEV_PRIVATE']
			signed_txn = web3.eth.account.sign_transaction(transaction, private_key)

			# 署名されたトランザクションを送信
			tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
			#st.success(f"購入手続きが完了しました。トランザクションハッシュ: {tx_hash.hex()}")
			# トランザクションの完了を待つ
			current_gas_price = web3.eth.gas_price
			st.write(f'Current network gas price: {web3.from_wei(current_gas_price, "gwei")} gwei')

			# トランザクションの詳細をログに出力
			st.write(f'Building transaction with nonce: {nonce}, gas: 2000000, gasPrice: 50 gwei')

			try:
				tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)  # 120秒でタイムアウト
				if tx_receipt.status == 1:
					st.success(f"購入手続きが完了しました。トランザクションハッシュ: {tx_hash.hex()}")
				else:
					st.error("トランザクションが失敗しました。")
			except TransactionNotFound:
				st.error("トランザクションが見つかりませんでした。")


		else:
			st.write('Please make sure you are connected to the network and all fields are correctly filled.')

	# 現在のCar Levelの表示
	if user_wallet_address:
		car_level = contract_object.functions.getCarLevel(user_wallet_address).call()
		st.write(f'Your current Car Level is: {car_level}')
