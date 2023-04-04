import pandas as pd
import streamlit as st
import numpy as np
import time
from PIL import Image
import datetime
import altair



st.title('飲食店データ webあぷり')
st.caption('Powered by k')
st.subheader('使い方 ガイド')
st.text('外食産業のデータの利活用を目的とした、WEBアプリ開発の試作品です。')
st.text('サイドバーに氏名などを登録してデータにアクセスしてください。')
image = Image.open('GPT.png')
st.sidebar.image(image,width=300)



with st.sidebar.form(key='profile_from'):

    start_date = st.date_input(
    '利用日 *',
    datetime.date(2023,3,29))
    company = st.selectbox(
        '会社名',
        ('株式会社','有限会社','合同会社'))
    Department = st.selectbox(
            '部署名（任意項目）*',
            ('本社営業部','大阪支店','名古屋支店','横浜支店','TCPリーシング課'))     
    name = st.text_input('氏名 *')
    Department = st.selectbox(
        '部署名(任意項目)',
        ('本社','支店'))
    access = st.radio(
        'アクセス先 *',
        ('会社','在宅'))
            # 複数選択
    Usage = st.multiselect(
            '用途 (複数選択可) *',
            ('営業資料','市場調査','データ分析','その他')
        
    resoiution = st.slider('chatGPT 解像度',0,100,50)
        
# ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル') 
if submit_btn:
    st.text(f'{name}さん、いらっしゃいませ！')
    
if submit_btn:
    df = pd.read_csv('tabe.csv', encoding='cp932')
    df = df.drop(['Tid','url','元値','集計用','食べログ業種_大','食べログ業種_中','食べログ業種_小','ジャンル'], axis=1)
    eria = st.text_input('駅指定（部分一致）')
    df= df[df['起点'].str.contains(eria)]#部分一致
    st.subheader('業種別')
    bar_df = pd.DataFrame(
        df['業態_集計用'].value_counts()
    )
    st.bar_chart(bar_df)
    st.dataframe(df)


