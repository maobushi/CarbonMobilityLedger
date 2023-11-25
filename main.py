import streamlit as st
from wallet_connect import wallet_connect
from streamlit_option_menu import option_menu
import time
import streamlit as st
from web3 import Web3
import os


contract_abi = open("abi.json", "r").read()


user_wallet_address = ""
contract = ""


# CBTトークンのバランスを取得
def get_cbt_balance(address):
    return contract.functions.balanceOf(address).call()

# Car Levelを取得
def get_car_level(address):
    return contract.functions.carLevel(address).call()







def plant_page():
	st.title("Plant")


def drive_page():
	st.title("Drive")

def buy_page():
	st.title("Buy")


# Custom CSS to position the navbar at the bottom

def home_page():
	selected2 = option_menu(None, ["Home", "Buy", "Drive", 'Plant'], 
		icons=['house', 'cart', 'car-front', 'tree-fill'], 
		menu_icon="cast", default_index=0, orientation="horizontal")
	
	cbt_balance = get_cbt_balance(user_wallet)
	car_level = get_car_level(user_wallet)

	st.write(f"CBTバランス: {cbt_balance}")
	st.write(f"Car Level: {car_level}")


	if selected2 == "Buy":
		buy_page()
		# InfuraのエンドポイントURLを使用（あなたのURLに置き換えてください）
		# 接続確認
		st.write(web3.is_connected())

	elif selected2 == "Drive":
		drive_page()
	elif selected2 == "Plant":
		plant_page()


## Streamlitアプリのタイトル
#st.title("Wallet Address Display")

#import streamlit as st
#from streamlit_option_menu import option_menu







# ログイン状態を管理
manage_session_state('logged_in', False)

# ログイン画面を表示する関数
def login_popup():
	with st.container():
		st.title("ログイン画面")
		st.empty()
		user_wallet_address = wallet_connect(label="wallet", key="wallet")
		#st.write("接続されたwallet アドレス")
		if user_wallet_address != "not":
			st.write(user_wallet_address)
		if user_wallet_address != None:
			st.session_state.logged_in = True


# メイン関数
def main():
	# ログインされていない場合は、ログイン画面を表示
	if not st.session_state.logged_in:
		login_popup()
	else:
		contract_address = "0x4DbBC6fA9C6e864D2264b68eCb787ed9E3EAbcB9"
		contract = web3.eth.contract(address=contract_address, abi=contract_abi)
		private_key = os.environ.get("METAMASK_DEV_PRIVATE")
		infura_url = "https://goerli.infura.io/v3/83987aa77bb741bba949a6e5b1f3ff07"
		web3 = Web3(Web3.HTTPProvider(infura_url))

		# トランザクションの送信者設定
		nonce = web3.eth.getTransactionCount(user_wallet_address)
		transaction = contract.functions.buyCar(10).buildTransaction({
			'gas': 2000000,
			'gasPrice': web3.toWei('50', 'gwei'),
			'from': user_wallet_address,
			'nonce': nonce
		})
		# ログイン済みの場合は、ホーム画面を表示
		home_page()

if __name__ == "__main__":
	main()

