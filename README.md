# Projeto-integrador - Mídias Sociais vs Produtividade (Grupo 13)
Desenvolvimento low code em ciência de dados

# Integrantes
* ⁠Adriano Barboza Rosa
* ⁠Emilly Gouveia Fortunato 
* Mariana dias
* Pedro Alvares Leite Carboni
* ⁠Guilherme Fernandes

## Estrutura de Pastas
O projeto seguirá a seguinte organização de diretórios:

* /data: Armazenará a base de dados original (base_original.csv) e a base após o tratamento (base_tratada.csv). 
* /src: Conterá os scripts Python focados no processo de ETL (etl.py).
* /app: Receberá o código-fonte responsável pela aplicação interativa e visualizações (dashboard.py).

## Objetivo
Investigar de forma mais aprofundada como os hábitos digitais cotidianos, como por exemplo a frequência de utilização de redes sociais, o tempo total de exposição às telas e a recorrência de notificações impactam diretamente aspectos como a produtividade, os níveis de estresse e o bem-estar geral de adultos inseridos em contextos que simulam situações reais do mercado de trabalho. A proposta busca compreender possíveis relações entre o comportamento digital e o desempenho em atividades profissionais, considerando fatores que podem contribuir tanto para a melhoria quanto para a queda de rendimento.

Para a realização dessa análise, será utilizada a base de dados pública [Social Media vs. Productivity](https://www.kaggle.com/datasets/mahdimashayekhi/social-media-vs-productivity), disponibilizada na plataforma Kaggle, permitindo a exploração de padrões, correlações e tendências relevantes.

## Tecnologias utilizadas
- Python
- Pandas
- SQLite
- Streamlit

## Planejamento:
* Tarefa 1 (Prazo: A DEFINIR): Extração e compreensão da base de dados do Kaggle - **Adriano Barboza Rosa**
  + **O que será feito:** Download da base, leitura inicial, entendimento e documentação dos dados e estrutura do dataset.
    
* Tarefa 2 (Prazo: A DEFINIR): Limpeza e tratamento de dados - ⁠**Emilly Gouveia Fortunato**
  + **O que será feito**: Tratamento de valores ausentes (NaN) nas colunas de 'sono' e 'estresse' via imputação de dados, além da identificação e remoção de valores atípicos (outliers) nas colunas de consumo de mídia, café e número de notificações.
    
* ⁠Tarefa 3 (Prazo: A DEFINIR): Transformação de Dados - **Mariana dias**
  + **O que será feito:** Criação de novas métricas secundárias, como tempo médio por plataforma, índice de uso digital
    
* ⁠Tarefa 4 (Prazo: A DEFINIR): Carga e armazenamento da base tratada em banco de dados - **Pedro Alvares Leite Carboni**
  + **O que será feito:** Exportação da base limpa, inserção no banco de dados (SQLite) e estruturação das informações para consumo pelo dashboard.
    
* Tarefa 5 (Prazo: A DEFINIR): Desenvolvimento do Dashboard interativo - ⁠**Guilherme Fernandes**
  + **O que será feito:** Desenvolvimento de dashboard utilizando a plataforma de criação de interfaces gráficas Streamlit, no ecossistema Python.

## Limpeza de dados e transformações:

A base de dados requer etapas de limpeza e transformação antes da realização da Análise Exploratória de Dados (EDA), com o objetivo de garantir a qualidade e a consistência das informações.

Em relação à limpeza, iremos identificar e tratar possíveis outliers, especialmente em variáveis como tempo de uso de redes sociais e horas de sono, que podem apresentar valores extremos e comprometer as análises. Para os valores nulos, utilizaremos a estratégia de imputação de dados (preenchimento com médias ou medianas), garantindo que registros incompletos importantes não sejam perdidos.. Por fim, iremos garantir a padronização dos dados de data e hora.

Sobre a transformação dos dados, iremos criar métricas secundárias, como por exemplo tempo médio por plataforma e agrupamentos por faixa etária.

## Dashboard / Visualizações e métricas
Para compreender melhor os dados e extrair insights relevantes, o dashboard será estruturado a partir de perguntas analíticas e métricas-chave relacionadas ao uso de redes sociais, hábitos diários e saúde mental, a partir das seguintes questões:

- Qual é o ranking das plataformas de redes sociais mais utilizadas?
- Qual é a média diária de uso das redes sociais?
- Qual é a média de horas de sono dos usuários?
- Quanto tempo, em média, os usuários passam em frente à tela antes de dormir?
- Como o nível de estresse varia por faixa etária?
- Qual é a média de dias em que os usuários sentem burnout por mês?

Para representar esses dados, serão utilizadas visualizações como gráficos de barras, gráficos de linha, gráficos de dispersão e cartões de KPI, permitindo tanto análises descritivas quanto a identificação de padrões.

Além disso, serão exploradas possíveis relações entre variáveis, como o impacto do uso de redes sociais sobre o sono, estresse e burnout, a fim de identificar tendências e correlações relevantes.
