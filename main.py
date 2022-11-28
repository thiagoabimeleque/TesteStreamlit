import streamlit as st
import pandas as pd
import yfinance as yf

df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTIFdx4Dc0bgMVULPPcUqRfA-a-ZUQ-GkXftTkSNS7R30IOKWismTNNwN-mmt2SVTP5Jynhi3rsEhm0/pub?gid=0&single=true&output=csv', decimal=",")

df['Total'] = df['Qtde'] * df['Preço']

option = st.sidebar.selectbox(
    'Selecione o Ativo',
     df['Ativo'].unique())

st.title("Ativo: " + option)
st.subheader(yf.download(option + '.SA', start="2022-11-28")['Adj Close'][0])
st.write(df.query(f'Ativo == "{option}"')['Total'].sum())
