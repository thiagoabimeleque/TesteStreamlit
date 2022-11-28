import streamlit as st
import pandas as pd
import yfinance as yf

df = pd.read_csv('', decimal=",")

df['Total'] = df['Qtde'] * df['Preço']

option = st.sidebar.selectbox(
    'Selecione o Ativo',
     df['Ativo'].unique())

st.title("Ativo: " + option)
st.subheader(round(yf.download(option + '.SA', start="2022-11-28")['Adj Close'][0],2))
st.write(df.query(f'Ativo == "{option}"')['Total'].sum())
