import streamlit as st
from datetime import datetime
import pandas as pd
import time

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
		st.session_state.earned_tokens = st.session_state.distance * 10  # 1kmあたり10CBT

		total_time = (datetime.now() - st.session_state.start_time).total_seconds()
		col1, col2, col3 = st.columns(3)
		col1.metric("現在の航続距離", f"{st.session_state.distance:.2f} km")
		col2.metric("獲得CBTトークン", f"{st.session_state.earned_tokens:.0f} CBT")
		col3.metric("走行時間", f"{total_time:.2f} 秒")

		# 運転停止ボタン（運転開始時のみ表示）
		if st.button('運転停止'):
			st.session_state.is_driving = False
			st.session_state.total_distance += st.session_state.distance
			st.session_state.total_earned_tokens += st.session_state.earned_tokens
			st.session_state.total_time += (datetime.now() - st.session_state.start_time).total_seconds()

		# 合計のメトリクスを表示
		col1, col2, col3 = st.columns(3)
		col1.metric("合計走行距離", f"{st.session_state.total_distance:.1f} km")
		col2.metric("合計獲得CBTトークン", f"{st.session_state.total_earned_tokens:.0f} CBT")
		col3.metric("合計走行時間", f"{st.session_state.total_time:.2f} 秒")
		while st.session_state.is_driving:
			time.sleep(1)
			st.experimental_rerun()
			# 運転停止ボタン（運転開始時のみ表示）

