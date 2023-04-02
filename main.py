import pandas as pd
import streamlit as st
import numpy as np
import time
from PIL import Image
import datetime
import altair



st.title('飲食店データ webあぷり')
st.caption('Powered by')
st.subheader('使い方 ガイド')
st.text('外食産業のデータの利活用を目的とした、WEBアプリ開発の試作品')
image = Image.open('GPT.png')
st.sidebar.image(image,width=300)

df = pd.read_csv('tabe.csv', encoding='cp932')
df = df.drop(['Tid','url','元値','集計用','食べログ業種_大','食べログ業種_中','食べログ業種_小','ジャンル'], axis=1)
eria = st.sidebar.text_input('駅指定（部分一致）')
df= df[df['起点'].str.contains(eria)]#部分一致
st.dataframe(df)

with st.sidebar.form(key='profile_from'):

    start_date = st.date_input(
    '利用日 *',
    datetime.date(2023,3,29))
    company = st.selectbox(
        '会社名',
        ('株式会社','有限会社','合同会社'))
    name = st.text_input('氏名 *')
    Department = st.selectbox(
        '部署名(任意項目)',
        ('本社','支店'))
    access = st.radio(
        'アクセス先 *',
        ('会社','在宅'))
    resoiution = st.slider('chatGPT 解像度',0,100,50)

st.subheader('業種別')
bar_df = pd.DataFrame(
    df['業態_集計用'].value_counts()
)
st.bar_chart(bar_df)
