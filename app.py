import streamlit as st
import pandas as pd
import random

# CSV読み込み
df = pd.read_csv('evaluation_words.csv')

st.title("評価語アンケートテンプレート生成ツール")

# カテゴリ選択 & 抽出語数
categories = df['感覚カテゴリ'].unique().tolist()
selected_categories = st.multiselect("評価したい感覚カテゴリを選んでください：", categories)
num_words = st.number_input("各カテゴリから抽出する評価語の数：", min_value=1, max_value=20, value=2, step=1)

# SessionStateに初期化
if "questions" not in st.session_state:
    st.session_state.questions = []

# ボタンを押したら質問をランダムに生成して保存
if st.button("テンプレート生成"):
    questions = []
    for category in selected_categories:
        words = df[df['感覚カテゴリ'] == category]['評価語'].tolist()
        selected = random.sample(words, min(num_words, len(words)))
        questions.extend(selected)
    st.session_state.questions = questions

# 生成済みの質問があるなら表示
if st.session_state.questions:
    st.subheader("生成された質問テンプレート：")
    for i, word in enumerate(st.session_state.questions):
        st.markdown(f"**Q{i+1}. 評価語「{word}」は、これらのサンプルを触って違いが分かると思いますか？**")
        st.radio("選択してください：", ["はい", "いいえ"], key=f"q{i+1}")
