import streamlit as st
from wallet_connect import wallet_connect
from streamlit_option_menu import option_menu
import time
import os
from pages.buy import buy_page
from pages.charge import charge_page
from pages.plant import plant_page
from pages.drive import drive_page
from initialdata import contract_address, contract_abi,  contract_object , private_key, infura_url
from web3 import Web3
from login import user_wallet_address
from streamlit_card import card

def home_page():

	user_wallet_address = st.session_state.get('user_wallet_address', None)
	checksum_address = Web3.to_checksum_address(user_wallet_address)
	#print(checksum_address)
	# 変換したアドレスを使用して、balanceOf と carLevel を呼び出す
	cbt_balance = contract_object.functions.balanceOf(checksum_address).call()
	car_level = contract_object.functions.getCarLevel(checksum_address).call()
	
	#cbt_balance = cbt_balance / 10 ** 18
	#cbt_balance_formatted = "{:.2f}".format(cbt_balance)

	#st.write(f"CBTバランス: {cbt_balance} CBT")  # 確認のための出力

	
	#cbt_num = f"{cbt_balance} <span style='font-size: 36px; font-weight: bold;'>CBT</span>"
	#html_template_cbt = """
	#<div style="position: relative; text-align: center; color: white;">
	#<img src="https://files.oaiusercontent.com/file-jEPTrFlwCN5Anzy0Ldap4AOb?se=2023-11-23T13%3A21%3A15Z&sp=r&sv=2021-08-06&sr=b&rscc=max-age%3D31536000%2C%20immutable&rscd=attachment%3B%20filename%3D7f8ad969-e620-4651-8599-1fb18b5f80d1.webp&sig=%2BhFWRoC5MLCQhhl6p2VH42VrXZkpUuTiYsG5ZW31Fp4%3D" alt="Your Image" style="width:100%; border-radius: 10px;">
	#<div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">
	#	<span style="background-color: rgba(0, 0, 0, 0.5); padding: 10px; border-radius: 5px; font-size: 70px; font-weight: bold;">{}</span>
	#</div>
	#</div>
	#"""
	#html_cbt = html_template_cbt.format(cbt_num)
	#st.markdown(html_cbt, unsafe_allow_html=True)
	# 以前のコード

	# スマートコントラクトから返されるバランスを取得
	raw_cbt_balance = contract_object.functions.balanceOf(checksum_address).call()
	distance = contract_object.functions.getDistance(checksum_address).call()

	# 取得したバランスの値を表示して確認

	# Ether単位に変換
	cbt_balance = raw_cbt_balance / 1e34
	cbt_balance_formatted = "{:.0f}".format(cbt_balance)



	carlevel_num = f"{car_level} <span style='font-size: 36px; font-weight: bold;'>Level</span>"
	html_template_cbt = """
	<div style="position: relative; text-align: center; color: white;">
	<img src="https://pbs.twimg.com/media/F_u9GVwbgAApLL_?format=jpg&name=medium" style="width:100%; height: 150px; border-radius: 10px; object-fit: cover;">
	<div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">
		<span style="background-color: rgba(0, 0, 0, 0.5); padding: 10px; border-radius: 5px; font-size: 70px; font-weight: bold;">{}</span>
	</div>
	</div>
	"""
	html_cbt = html_template_cbt.format(carlevel_num)
	st.markdown(html_cbt, unsafe_allow_html=True)
	# cbt_balance の代わりに cbt_balance_formatted を使用
	#cbt_num = f"{cbt_balance_formatted} <span style='font-size: 36px; font-weight: bold;'>CBT</span>"
	st.empty()
	st.text("")
	
	cbt_balance_formatted = f"{cbt_balance_formatted} <span style='font-size: 36px; font-weight: bold;'>CBT</span>"
	html_template_cbt = """
		<div style="position: relative; text-align: center; color: white;">
		<img src="https://pbs.twimg.com/media/F_u9HMiaEAA-sO5?format=jpg&name=medium" alt="Your Image" style="width:100%; height: 150px; border-radius: 10px; object-fit: cover;">
		<div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">
			<span style="background-color: rgba(0, 0, 0, 0.5); padding: 10px; border-radius: 5px; font-size: 70px; font-weight: bold; white-space: nowrap;">{}</span>
		</div>
		</div>
	"""
	html_cbt = html_template_cbt.format(cbt_balance_formatted)
	st.markdown(html_cbt, unsafe_allow_html=True)


	st.empty()
	st.text("")
	distance = distance / (10 ** 18)
	distance = f"{distance:.1f} <span style='font-size: 36px; font-weight: bold;'>km</span>"
	html_distance = """
		<div style="position: relative; text-align: center; color: white;">
		<img src="https://pbs.twimg.com/media/F_vq-tnbIAAAEwt?format=jpg&name=large" alt="Your Image" style="width:100%; height: 150px; border-radius: 10px; object-fit: cover;">
		<div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">
			<span style="background-color: rgba(0, 0, 0, 0.5); padding: 10px; border-radius: 5px; font-size: 70px; font-weight: bold; white-space: nowrap;">{}</span>
		</div>
		</div>
	"""
	html_cbt = html_distance.format(distance)
	st.markdown(html_cbt, unsafe_allow_html=True)





