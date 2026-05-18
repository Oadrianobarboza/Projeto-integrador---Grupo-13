import streamlit as st
import pandas as pd
import sqlite3

st.title("Mídias Sociais vs Produtividade 📊")
#df = pd.read_csv('data/dataset_limpo (1).csv')

# Novo código lendo do banco de dados:
conn = sqlite3.connect('banco_projeto.db')
df = pd.read_sql('SELECT * FROM dados_produtividade', conn)
conn.close()

# Criando 3 colunas para as métricas no topo usando as colunas reais do seu arquivo
col1, col2, col3 = st.columns(3)
col1.metric("Média de Idade", round(df['age'].mean(), 2))
col2.metric("Tempo Médio de Mídia (h)", round(df['daily_social_media_time'].mean(), 2))
col3.metric("Média de Sono (h)", round(df['sleep_hours'].mean(), 2))

st.write("---") # Linha divisória

# Mantendo o nosso gráfico de barras
st.write("Quais são as redes sociais mais acessadas pelos usuários?")
st.bar_chart(df['social_platform_preference'].value_counts())