import streamlit as st
from wallet_connect import wallet_connect
from streamlit_option_menu import option_menu
import time
import os
from pages.buy import buy_page
from pages.plant import plant_page
from pages.drive import drive_page
from pages.home import home_page
from pages.charge import charge_page
from web3 import Web3
from initialdata import contract_address, contract_abi,  contract_object , private_key, infura_url
from login import user_wallet_address


def lobby_page():
	st.title("Carbon Token App")
	selected2 = option_menu(None, ["Home", "Buy", "Drive", 'Charge','Plant'], 
		icons=['house', 'cart', 'car-front', 'battery-charging' , 'tree-fill'], 
		menu_icon="cast", default_index=0, orientation="horizontal")
	

	if selected2 == "Home":
		home_page()
	if selected2 == "Buy":
		buy_page()
	elif selected2 == "Drive":
		drive_page()
	elif selected2 == "Charge":
		charge_page()
	elif selected2 == "Plant":
		plant_page()

 