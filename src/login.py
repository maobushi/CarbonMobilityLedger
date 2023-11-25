import streamlit as st
from wallet_connect import wallet_connect
from streamlit_option_menu import option_menu
import time
import streamlit as st
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
        st.empty()
        user_wallet_address = wallet_connect(label="wallet", key="wallet")
        if user_wallet_address != "not" and user_wallet_address is not None:
            st.session_state.user_wallet_address = user_wallet_address
            st.session_state.logged_in = True

