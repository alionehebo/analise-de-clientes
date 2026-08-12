import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

# Configuração da página do Streamlit
st.set_page_config(
    page_title="Análise de Retenção e Cancelamento de clientes",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Estilo visual limpo
sns.set_theme(style="white")

# 1. Carregar os Dados (com cache para ficar super rápido)


@st.cache_data
def carregar_dados():
  return pd.read_csv("dados_tratados.csv")


dados = carregar_dados()

# -----------------------------------------------------------------------------
# CABEÇALHO & STORYTELLING DE IMPACTO
# -----------------------------------------------------------------------------
st.title("Painel de Retenção e Análise de Churn (Cancelamento)")
st.markdown("""
Esse painel é um relatório visual interativo que permite analisar o comportamento de cancelamento (churn) dos clientes da Hori SaaS.
Ele fornece insights sobre os fatores que influenciam o churn, permitindo que a equipe de marketing e produto tome decisões informadas para melhorar a retenção de clientes.
""")

st.divider()

#indicadores de topo KPIs
col1, col2, col3 = st.columns(3)
total_clientes = len(dados)
churn_atual = dados["cancelou"].mean() * 100

col1.metric("Total de clientes", f"{total_clientes:,.0f}")
col2.metric("Taxa de Churn Atual", f"{churn_atual:.1f}%", delta="-Crítico", delta_color="inverse")
col3.metric("Meta de Churn Simulado", "18.4%", delta="+38.4%")

st.divider()

#ESTRUTURA DE ABAS
aba1, aba2, aba3, aba4 = st.tabs([
    "1. Problema do produto (contratos)",
    "2. Problema operacional (suporte)",
    "3. Simulação de impacto",
    "4. Número de clientes",
])

#Painel 1: Contratos
with aba1:
    st.subheader("1. O problema do plano mensal")
    st.write(
        "Clientes com contratos mensais apresentam uma taxa de 100% de cancelamento"
        "O que representa o maior desafio de retenção da empresa"
    )
    df_contrato = (
        dados.groupby("duracao_contrato")["cancelou"].mean().reset_index()
    )
    df_contrato["cancelou"] = df_contrato["cancelou"] * 100

    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(
        data=df_contrato,
        x="duracao_contrato",
        y="cancelou",
        palette=["#1f77b4", "#ff7f0e", "#2ca02c"],
        ax=ax,
    )
    ax.set_ylabel("Taxa de Churn(%)")
    ax.set_xlabel("Tipo de contrato")
    ax.set_ylim(0, 115)
    sns.despine()

    for p in ax.patches:
        ax.annotate(
            f"{p.get_height():.1f}%",
            (p.get_x() + p.get_width() / 2.0, p.get_height()),
            ha="center",
            va="bottom",
            xytext=(0, 5),
            textcoords="offset points",
            fontweight="bold",
        )
        st.pyplot(fig)

# --- ABA 3: SIMULAÇÃO INTERATIVA ---
with aba3:
  st.subheader("3. Simulação de Cenários em Tempo Real")
  st.write(
      "Ajuste os filtros interativos na barra lateral para simular novas réguas"
      " de negócio!"
  )

  # Filtros Interativos na Barra Lateral
  st.sidebar.header("⚙️ Filtros de Simulação")

  remover_mensal = st.sidebar.checkbox("Remover Contrato Mensal", value=True)
  max_ligacoes = st.sidebar.slider(
      "Máximo de Ligações Permitidas", 1, 10, value=4
  )
  max_atraso = st.sidebar.slider(
      "Máximo de Dias de Atraso Tolerável", 1, 30, value=20
  )

  # Filtrando a base dinamicamente
  dados_simulados = dados.copy()

  if remover_mensal:
    dados_simulados = dados_simulados[
        dados_simulados["duracao_contrato"] != "Monthly"
    ]

  dados_simulados = dados_simulados[
      (dados_simulados["ligacoes_callcenter"] <= max_ligacoes)
      & (dados_simulados["dias_atraso"] <= max_atraso)
  ]

  novo_churn = dados_simulados["cancelou"].mean() * 100
  clientes_restantes = len(dados_simulados)

  st.success(f"**Nova Taxa de Churn Simulado:** {novo_churn:.2f}%")
  st.info(f"**Total de Clientes Retidos no Cenário:** {clientes_restantes:,.0f}")

# --- ABA 4: EXPLORAÇÃO DA BASE ---
with aba4:
  st.subheader("Visualização da Base Tratada")
  st.dataframe(dados.head(100))