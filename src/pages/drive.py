import streamlit as st
from datetime import datetime
import pandas as pd
import time
from web3.exceptions import TransactionNotFound
import os
from initialdata import contract_address, contract_abi,  contract_object , private_key, infura_url, web3

def drive_page():
	# セッションステートの初期化
	if 'is_driving' not in st.session_state:
		st.session_state.is_driving = False
	if 'start_time' not in st.session_state:
		st.session_state.start_time = 0
	if 'distance' not in st.session_state:
		st.session_state.distance = 0.0
	if 'earned_tokens' not in st.session_state:
		st.session_state.earned_tokens = 0
	if 'total_distance' not in st.session_state:
		st.session_state.total_distance = 0.0
	if 'total_earned_tokens' not in st.session_state:
		st.session_state.total_earned_tokens = 0
	if 'total_time' not in st.session_state:
		st.session_state.total_time = 0

	# 現在地の緯度と経度
	latitude = 35.6895  # 東京の緯度
	longitude = 139.6917  # 東京の経度

	# 地図の表示用データフレームの作成
	df = pd.DataFrame({'lat': [latitude], 'lon': [longitude]})

	# 地図の表示
	st.map(df)

	# 運転開始ボタン
	if st.button('運転開始'):
		st.session_state.is_driving = True
		st.session_state.start_time = datetime.now()

	# 運転中の処理
	if st.session_state.is_driving:
		current_time = datetime.now()
		time_diff = (current_time - st.session_state.start_time).total_seconds()
		st.session_state.distance = time_diff / 30  # 30秒に1km
		st.session_state.earned_tokens = st.session_state.distance * 1  # 1kmあたり10CBT

		total_time = (datetime.now() - st.session_state.start_time).total_seconds()
		col1, col2, col3 = st.columns(3)
		col1.metric("現在の航続距離", f"{st.session_state.distance:.2f} km")
		col2.metric("獲得CBTトークン", f"{st.session_state.earned_tokens:.0f} CBT")
		col3.metric("走行時間", f"{total_time:.2f} 秒")

		# 運転停止ボタン（運転開始時のみ表示）
		
		# 運転停止ボタン（運転開始時のみ表示）
		if st.button('運転停止'):
			st.session_state.is_driving = False
			distance_driven = st.session_state.distance
			st.session_state.total_distance += distance_driven
			st.session_state.total_earned_tokens += st.session_state.earned_tokens
			st.session_state.total_time += (datetime.now() - st.session_state.start_time).total_seconds()

			# トランザクションの構築と送信
			user_wallet_address = st.session_state.user_wallet_address
			nonce = web3.eth.get_transaction_count(user_wallet_address)
			distance_driven_wei = int(distance_driven * 1e18)  # Wei単位への変換
			transaction = contract_object.functions.driveCar(distance_driven_wei).build_transaction({
				'chainId': 5,
				'gas': 2000000,
				'gasPrice': web3.to_wei('50', 'gwei'),
				'from': user_wallet_address,
				'nonce': nonce
			})
			# トランザクションの署名
			private_key = os.environ['METAMASK_DEV_PRIVATE']
			signed_txn = web3.eth.account.sign_transaction(transaction, private_key)

			# トランザクションの送信
			try:
				tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
				tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)
				if tx_receipt.status == 1:
					st.success(f"走行手続きが完了しました。トランザクションハッシュ: {tx_hash.hex()}")
				else:
					st.error("トランザクションが失敗しました。")
			except TransactionNotFound:
				st.error("トランザクションが見つかりませんでした。")

		# 合計のメトリクスを表示
		col1, col2, col3 = st.columns(3)
		col1.metric("合計走行距離", f"{st.session_state.total_distance:.1f} km")
		col2.metric("合計獲得CBTトークン", f"{st.session_state.total_earned_tokens:.0f} CBT")
		col3.metric("合計走行時間", f"{st.session_state.total_time:.2f} 秒")
		while st.session_state.is_driving:
			time.sleep(1)
			st.experimental_rerun()
			# 運転停止ボタン（運転開始時のみ表示）

