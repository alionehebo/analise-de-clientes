<!-- Badge (Botão) da app -->
[![Streamlit App](https://streamlit.io)](https://datacustomer.streamlit.app/)

# 📊 Análise de Cancelamento de Clientes

## 🎯 1. O Problema de Negócio (Impacto)

A retenção de clientes é a métrica mais crítica para a sustentabilidade da empresa. Este projeto foi desenvolvido para identificar os fatores que levam os clientes a cancelar o serviço (churn) e criar uma ferramenta que permita à gestão da empresa compreender os factores que influenciam no cancelamento de clientes e desse modo melhorar na eficiência operacional.
---

## 🚀 2. A Solução (A Aplicação Streamlit)

Desenvolvi uma aplicação interativa que transforma dados complexos em decisões acionáveis para o negócio.

* **Painel Executivo:** Visualização geral das taxas de churn.
* **Análise de Risco:** Identificação dos principais gatilhos (triggers) de cancelamento (ex: problemas no suporte, preço do contrato).
* **Simulador de Retenção:** Uma ferramenta onde a equipa pode simular descontos ou campanhas e ver o impacto imediato na probabilidade de o cliente ficar.

---

## 📈 3. Principais Insights de Negócio
*Quais foram as grandes descobertas dos dados?*

1. **Problema do Suporte:** Clientes que abriram mais de 4 vezes no suporte e com atraso de 25-30 dias têm **80% de probabilidade** de cancelar nos 30 dias seguintes.
2. **Tipo de Contrato:** Contratos mensais apresentam uma taxa de churn **100%** que representa o maior desafio de retenção da empresaanálise.
---

## 🛠️ 4. Stack Tecnológica e Metodologia
*Ferramentas usadas*

* **Linguagem:** Python
* **Análise de Dados:** Pandas, NumPy
* **Visualização:** Matplotlib, Seaborn, Plotly (Gráficos Interativos)
* **Interface / Deploy:** Streamlit & Streamlit Community Cloud

---

## 📂 5. Estrutura do Repositório
*Organização limpa do projeto.*

```text
├── app.py               # Código principal da aplicação Streamlit
├── dados_tratados.csv   # Bases de dados (dataset no formato CSV)
└── README.md            # Documentação principal
├── requirements.txt     # Dependências do projeto

```

---

## ⚙️ 6. Como Executar o Projeto Localmente
*Instruções rápidas para técnicos que queiram testar o código.*

1. Clone o repositório:
   ```bash
   git clone https://github.com/alionehebo/analise-de-clientes.git
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute a aplicação:
   ```bash
   streamlit run app.py
   ```

---
## 👤 7. Contacto e Links
Sinta-se a vontade para me contactar em nos seguintes meios:
[![LinkedIn](https://shields.io)](https://www.linkedin.com/in/alione-hebo-ab464b2b4/)
[![E-mail](https://shields.io)](mailto:alionehebo05@gmail.com)
