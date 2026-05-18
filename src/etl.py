import pandas as pd
import sqlite3

print("1. Extraindo dados...")
# Lendo o arquivo original do Kaggle
df = pd.read_csv('data/base_original_social_media_vs_productivity.csv') 

print("2. Transformando dados...")
df['sleep_hours'] = df['sleep_hours'].fillna(df['sleep_hours'].mean())
df['stress_level'] = df['stress_level'].fillna(df['stress_level'].mean())
df['indice_uso_digital'] = df['daily_social_media_time'] / df['sleep_hours']

print("3. Carregando no banco de dados...")
conn = sqlite3.connect('banco_projeto.db')
df.to_sql('dados_produtividade', conn, if_exists='replace', index=False)
conn.close()

print("Processo de ETL concluído com sucesso!")
