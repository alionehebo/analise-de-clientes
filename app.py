import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

# -----------------------------------------------------------------------------
# 1. CONFIGURAÇÃO DA PÁGINA
#-----------------------------------------------------------------------------
st.set_page_config(
    page_title='Hori SaaS - Diagnóstico de Churn',
    page_icon='📊',
    layout='wide',
)

# Estilo global simples do Seaborn
sns.set_theme(style='white')


# -----------------------------------------------------------------------------
# 2. CARREGAMENTO DOS DADOS (Simulado / Substitua pelo seu DataFrame)
# -----------------------------------------------------------------------------
@st.cache_data
def carregar_dados():
  return pd.read_csv('dados_tratados.csv')


try:
  dados_tratados = carregar_dados()
except Exception:
  st.warning(
      '⚠️ Certifique-se de que a base de dados tratada está acessível no'
      ' script.'
  )
  st.stop()

# -----------------------------------------------------------------------------
# 3. CABEÇALHO PRINCIPAL
# -----------------------------------------------------------------------------
st.title('📊 Diagnóstico Estratégico de Churn — Hori SaaS')
st.markdown(
    '### *Transformando dados operacionais em planos de retenção de clientes*'
)
st.divider()

# -----------------------------------------------------------------------------
# 4. ESTRUTURA DE STORYTELLING (ABAS / SLIDES)
# -----------------------------------------------------------------------------
aba1, aba2, aba3 = st.tabs([
    '🔴 1. O Problema do Produto',
    '🟡 2. O Ponto de Ruptura',
    '🟢 3. O Impacto da Solução',
])

# =============================================================================
# SLIDE 1: O PROBLEMA DO PRODUTO (CONTRATO MENSAL)
# =============================================================================
with aba1:
  st.header('Ataque ao Gargalo Comercial')

  # Citação / Mensagem Central
  st.info(
      '💡 **Insight Principal:** *"Olhem para esta barra vermelha: 100% dos'
      ' clientes mensais nos deixam. Nosso primeiro foco estratégico deve ser a'
      ' reestruturação desse contrato."*'
  )

  col1, col2 = st.columns([1, 2])

  with col1:
    st.markdown('### 📌 Métricas Chave')
    total_mensal = (dados_tratados['duracao_contrato'] == 'Monthly').sum()
    st.metric(label='Clientes no Plano Mensal', value=f'{total_mensal:,}')
    st.metric(
        label='Taxa de Cancelamento (Mensal)',
        value='100%',
        delta='-100% Retenção',
        delta_color='inverse',
    )

    st.markdown("""
        **Diagnóstico de Negócio:**
        * O plano mensal funciona hoje como um ralo de clientes.
        * Praticamente **20% de toda a base** entra por esta modalidade e cancela em seguida.
        
        **Ação Recomendada:**
        * Descontinuar o plano mensal simples ou aplicar período mínimo de fidelidade (3 meses).
        * Oferecer descontos atrativos para migração automática aos planos Anual e Trimestral.
        """)

  with col2:
    # Gráfico 1
    fig1, ax1 = plt.subplots(figsize=(7, 4))
    df_contrato = (
        dados_tratados.groupby('duracao_contrato')['cancelou']
        .mean()
        .reset_index()
    )
    df_contrato['cancelou'] = df_contrato['cancelou'] * 100

    sns.barplot(
        data=df_contrato,
        x='duracao_contrato',
        y='cancelou',
        palette=['#34495e', '#e74c3c', '#34495e'],
        ax=ax1,
    )

    ax1.set_title(
        'Taxa de Churn por Tipo de Contrato (%)',
        fontsize=12,
        fontweight='bold',
    )
    ax1.set_xlabel('Tipo de Contrato')
    ax1.set_ylabel('Taxa de Churn (%)')
    ax1.set_ylim(0, 115)
    sns.despine(top=True, right=True)

    for p in ax1.patches:
      height = p.get_height()
      ax1.annotate(
          f'{height:.1f}%',
          (p.get_x() + p.get_width() / 2.0, height),
          ha='center',
          va='bottom',
          xytext=(0, 5),
          textcoords='offset points',
          fontweight='bold',
      )

    st.pyplot(fig1)

# =============================================================================
# SLIDE 2: O PONTO DE RUPTURA (CALL CENTER)
# =============================================================================
with aba2:
  st.header('Gargalo de Atendimento e Suporte')

  st.warning(
      '💡 **Insight Principal:** *"Aqui está o nosso segundo alerta: vejam a'
      ' curva subir abruptamente. A partir da 5ª ligação ao suporte, perdemos o'
      ' cliente. A 4ª ligação precisa ser o nosso gatilho vermelho no CRM."*'
  )

  col1, col2 = st.columns([1, 2])

  with col1:
    st.markdown('### 📌 Métricas Chave')
    st.metric(label='Limite Tolerável de Atendimento', value='3 Ligações')
    st.metric(
        label='Churn a partir da 5ª Ligaçâo',
        value='94.5%',
        delta='Zona Crítica',
        delta_color='inverse',
    )

    st.markdown("""
        **Diagnóstico de Negócio:**
        * Clientes que ligam até 2 vezes mantêm um Churn controlado (~30%).
        * A partir da **4ª ligação**, a tolerância acaba e a probabilidade de cancelamento dispara.
        
        **Ação Recomendada:**
        * **Regra de Ouro no CRM:** Disparar alerta imediato de Customer Success quando o cliente abrir o 4º chamado.
        * Resolução prioritária e personalizada antes que o cliente atinja o 5º contato.
        """)

  with col2:
    # Gráfico 2
    fig2, ax2 = plt.subplots(figsize=(7, 4))
    df_suporte = (
        dados_tratados.groupby('ligacoes_callcenter')['cancelou']
        .mean()
        .reset_index()
    )
    df_suporte['cancelou'] = df_suporte['cancelou'] * 100

    sns.lineplot(
        data=df_suporte,
        x='ligacoes_callcenter',
        y='cancelou',
        marker='o',
        color='#e74c3c',
        linewidth=2.5,
        markersize=7,
        ax=ax2,
    )

    ax2.axvline(
        x=4,
        color='#7f8c8d',
        linestyle='--',
        linewidth=1.5,
        label='Alerta (4ª Ligação)',
    )
    ax2.axvspan(
        4.5, 10, color='#e74c3c', alpha=0.1, label='Zona Crítica (> 90%)'
    )

    ax2.set_title(
        'O Ponto de Ruptura no Atendimento', fontsize=12, fontweight='bold'
    )
    ax2.set_xlabel('Número de Ligações ao Call Center')
    ax2.set_ylabel('Taxa de Churn (%)')
    ax2.set_ylim(0, 110)
    ax2.set_xticks(range(0, 11))
    ax2.legend(loc='upper left', frameon=True)
    sns.despine(top=True, right=True)

    st.pyplot(fig2)

# =============================================================================
# SLIDE 3: O IMPACTO DA SOLUÇÃO (COMPARATIVO)
# =============================================================================
with aba3:
  st.header('Resultado Projetado com o Plano de Ação')

  st.success(
      '💡 **Insight Principal:** *"Se atuarmos nesses dois pontos e na cobrança'
      ' preventiva, este é o resultado: reduzimos o churn de 56.8% para 18.4%,'
      ' salvando mais de 26 mil clientes."*'
  )

  col1, col2 = st.columns([1, 2])

  # Calculando a métrica dinâmica para garantir precisão
  cenario_ideal = dados_tratados[
      (dados_tratados['duracao_contrato'] != 'Monthly')
      & (dados_tratados['ligacoes_callcenter'] < 5)
      & (dados_tratados['dias_atraso'] <= 20)
  ]
  taxa_simulada = cenario_ideal['cancelou'].mean() * 100
  clientes_salvos = len(cenario_ideal)

  with col1:
    st.markdown('### 📌 Impacto Final')
    st.metric(
        label='Churn Atual (Real)', value='56.8%', delta_color='off'
    )
    st.metric(
        label='Churn Projetado (Simulado)',
        value=f'{taxa_simulada:.1f}%',
        delta='-38.4% de Redução',
        delta_color='normal',
    )
    st.metric(label='Clientes Preservados na Base', value=f'{clientes_salvos:,}')

    st.markdown("""
        **Resumo Executivo:**
        * A aplicação das 3 correções simples transforma o negócio de um estado **crítico** para um estado **saudável e escalável**.
        * Uma taxa de **18.4%** coloca a Hori SaaS dentro dos padrões ideais do mercado internacional.
        """)

  with col2:
    # Gráfico 3
    fig3, ax3 = plt.subplots(figsize=(6, 4))
    df_comparativo = pd.DataFrame({
        'Cenário': ['Cenário Atual', 'Cenário Simulado'],
        'Churn': [dados_tratados['cancelou'].mean() * 100, taxa_simulada],
    })

    sns.barplot(
        data=df_comparativo,
        x='Cenário',
        y='Churn',
        palette=['#e74c3c', '#27ae60'],
        width=0.4,
        ax=ax3,
    )

    ax3.set_title(
        'Redução Potencial da Taxa de Churn', fontsize=12, fontweight='bold'
    )
    ax3.set_xlabel('')
    ax3.set_ylabel('Taxa de Churn (%)')
    ax3.set_ylim(0, 75)
    sns.despine(top=True, right=True)

    for p in ax3.patches:
      height = p.get_height()
      ax3.annotate(
          f'{height:.1f}%',
          (p.get_x() + p.get_width() / 2.0, height),
          ha='center',
          va='bottom',
          xytext=(0, 5),
          textcoords='offset points',
          fontweight='bold',
      )

    st.pyplot(fig3)