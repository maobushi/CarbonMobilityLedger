import streamlit as st
from wallet_connect import wallet_connect
from streamlit_option_menu import option_menu
import time
import streamlit as st
from web3 import Web3
import os
from streamlit_card import card
from initialdata import contract_address, contract_abi,  contract_object , private_key, infura_url, web3
from web3.exceptions import TransactionNotFound



def buy_page():
	def show_purchase_option(title, price):
		carbon_token = price * 0.01
		carbon_token_wei = int(carbon_token * 1e18) 
		with st.expander(f"{title} 購入オプション"):
			st.write(f"購入予定価格: ¥{price:,} (消費税込)")
			st.write(f"付与予定のカーボントークン: {carbon_token} CBT")
			if st.button(f"{title} 購入確定"):
				user_wallet_address = st.session_state.user_wallet_address
				nonce = web3.eth.get_transaction_count(user_wallet_address)
				transaction = contract_object.functions.buyCar(carbon_token_wei).build_transaction({
				'chainId': 5,
				'gas': 2000000,
				'gasPrice': web3.to_wei('50', 'gwei'),
				'from': user_wallet_address,
				'nonce': nonce
				})
				# ここでトランザクションを署名する
				private_key = os.environ['METAMASK_DEV_PRIVATE']
				signed_txn = web3.eth.account.sign_transaction(transaction, private_key)

				# 署名されたトランザクションを送信
				tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
				#st.success(f"購入手続きが完了しました。トランザクションハッシュ: {tx_hash.hex()}")
				# トランザクションの完了を待つ
				try:
					tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)  # 120秒でタイムアウト
					if tx_receipt.status == 1:
						st.success(f"購入手続きが完了しました。トランザクションハッシュ: {tx_hash.hex()}")
					else:
						st.error("トランザクションが失敗しました。")
				except TransactionNotFound:
					st.error("トランザクションが見つかりませんでした。")


	def dummy_function():
		pass

	hasClickedRotary = card(
		title="ROTARY-EV",
		text="e-SKYACTIV R-EV",
		image="https://www.mazda.co.jp/globalassets/assets/cars/mx-30/model/230914_hero_mx30_grade_01_engine_03.jpg",
		on_click=dummy_function
	)
	if hasClickedRotary:
		show_purchase_option("Edition R", 4917000)
		show_purchase_option("Natural Monotone", 4785000)
		show_purchase_option("Rotary-EV", 495000)

	hasClickedEv = card(
		title="EV",
		text="e-SKYACTIV EV",
		image="https://www.mazda.co.jp/globalassets/assets/cars/mx-30/model/230914_hero_mx30_grade_01_engine_02.jpg",
		on_click=dummy_function
	)
	if hasClickedEv:
		show_purchase_option("EV", 4510000)
		show_purchase_option("EV Basic Set", 4587000)
		show_purchase_option("EV Highest Set", 5016000)

	hasClickedHybrid = card(
		title="Hybrid",
		text="e-SKYACTIV EV",
		image="https://www.mazda.co.jp/globalassets/assets/cars/mx-30/model/230914_hero_mx30_grade_01_engine_01.jpg",
		on_click=dummy_function
	)
	if hasClickedHybrid:
		show_purchase_option("MX-30", 2640000)
		show_purchase_option("Industrial Classic", 2761000)