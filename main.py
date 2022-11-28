import streamlit as st
import pandas as pd

df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTIFdx4Dc0bgMVULPPcUqRfA-a-ZUQ-GkXftTkSNS7R30IOKWismTNNwN-mmt2SVTP5Jynhi3rsEhm0/pub?gid=0&single=true&output=csv', decimal=",")

df['Total'] = df['Qtde'] * df['Preço']

option = st.sidebar.selectbox(
    'Selecione o Ativo',
     df['Ativo'].unique())

st.title('title')
st.subheader("Ativo: " + option)
st.write(df.query(f'Ativo == "{option}"')['Total'].sum())



