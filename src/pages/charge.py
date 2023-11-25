import streamlit as st
from wallet_connect import wallet_connect
from streamlit_option_menu import option_menu
import time
import streamlit as st
from web3 import Web3
import os

from initialdata import contract_address, contract_abi,  contract_object , private_key, infura_url
def charge_page():


	# 価格設定
	kwh_price = 30  # 1kWhあたりの価格

	# 価格の表示
	st.info(f"現在の1kWhあたりの価格: {kwh_price}円")

	# kWhの入力（スライドバー）
	kwh = st.slider('充電するkWhを選択', min_value=0.0, max_value=35.5, step=0.1)

	# CBTトークンの入力
	cbt_tokens = st.number_input('使用するCBTトークン量を入力', min_value=100, step=100, format="%d")

	# 請求金額の計算
	billing_amount = max(0, (kwh * kwh_price) - cbt_tokens)  # 請求金額がマイナスにならないように調整
	st.info(f"請求金額: {billing_amount}円")

	# キャッシュバック量の計算
	cashback_cbt = billing_amount * 0.01  # 請求金額の1%
	st.info(f"獲得予定 CBT量: {cashback_cbt}CBT")

	st.empty()
	# 充電ボタンと進捗バー
	if st.button('充電'):
		progress_bar = st.progress(0)
		for percent_complete in range(100):
			time.sleep(0.05)
			progress_bar.progress(percent_complete + 1)
		st.success('充電完了')
		st.success(f"獲得CBT量: {cashback_cbt}CBT")
