import streamlit as st
from wallet_connect import wallet_connect
from streamlit_option_menu import option_menu
from login import login_popup , manage_session_state
import time
import streamlit as st
from web3 import Web3
import os
from pages.lobby import lobby_page


# メイン関数
def main():
	# ログイン状態を管理
	manage_session_state('logged_in', False)

	# ログインされていない場合は、ログイン画面を表示
	if not st.session_state.logged_in:
		login_popup()
	else:
		#web3 = Web3(Web3.HTTPProvider(infura_url))

		## トランザクションの送信者設定
		#nonce = web3.eth.getTransactionCount(user_wallet_address)
		#transaction = contract.functions.buyCar(10).buildTransaction({
		#	'gas': 2000000,
		#	'gasPrice': web3.toWei('50', 'gwei'),
		#	'from': user_wallet_address,
		#	'nonce': nonce
		#})
		## ログイン済みの場合は、ホーム画面を表示
		lobby_page()

if __name__ == "__main__":
	main()

