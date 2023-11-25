import streamlit as st
from wallet_connect import wallet_connect
from streamlit_option_menu import option_menu
import time
from web3 import Web3
import os

user_wallet_address = None

# Streamlitcのセッション状態を管理するための関数
def manage_session_state(key, initial_value):
    if key not in st.session_state:
        st.session_state[key] = initial_value




# ログイン画面を表示する関数
def login_popup():
    with st.container():
        st.title("Carbon Drive")
        st.write("Login with your wallet")  
        
        user_wallet_address = wallet_connect(label="wallet", key="wallet")
        if user_wallet_address != "not" and user_wallet_address is not None:
            st.session_state.user_wallet_address = user_wallet_address

            # 免許証入力欄
            license_number = st.text_input("Enter your driver's license number")
            # 車体番号入力欄
            vin_number = st.text_input("Enter your vehicle identification number (VIN)")

            # 確認ボタン
            if st.button('Confirm'):
                # 入力された情報をセッション状態に保存
                st.info('Logging Wallet Address: ' + user_wallet_address)
                st.session_state.license_number = license_number
                st.session_state.vin_number = vin_number
                st.success('Login Successful!')
                st.session_state.logged_in = True