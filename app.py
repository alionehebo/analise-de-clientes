import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

#configuração da página streamlit
st.set_page_config(
    page_title="Análise de Churn",
    layout="wide",
    initial_sidebar_state="expanded",
)

#estilo visual limpo
sns.set_theme(style="red")

# Etapa 1: carregar o dataset (com o cache para aumentar a velocidade)
@st.cache_data
def carregar_dados():
    return pd.read_csv("dados_tratados_csv")

dados = carregar_dados()
