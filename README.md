<!-- Badge (Botão) da app -->

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-red?logo=streamlit)

* 🚀 **App Interativo (Streamlit):** [Acessar Dashboard Web](https://datacustomer.streamlit.app/)

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

1. **Tipo de Contrato:** Contratos mensais apresentam uma taxa de churn **100%** que representa o maior desafio de retenção da empresaanálise.
2. **Problema do Suporte:** | **94,5% a 100% de Churn** a partir da 5ª ligação | O cliente que liga 5 ou mais vezes para o Call Center atinge o ponto de ruptura e abandona a plataforma. |
| **3. Inadimplência Prolongada** | **100% de Churn** após 20 dias de atraso | Atrasos acima de 20 dias resultam em perda total do cliente (possível corte automático de sistema ou desistência). |

Ao aplicar filtros estratégicos na base para simular a resolução desses gargalos operacionais e comerciais:
1. Reestruturação do plano mensal;
2. Resolução de problemas no suporte em até 4 ligações;
3. Régua de cobrança preventiva para evitar pendências acima de 20 dias.

```text
[Cenário Atual]   Taxa de Churn: 56.8%  ████████████████████████ (Crítico)
[Cenário Ideal]   Taxa de Churn: 18.4%  ████████ (Saudável)
-------------------------------------------------------------------------
Impacto Direto:   Queda de 38.4 pontos percentuais no Churn.
Clientes Salvos:  26.269 clientes preservados na base.
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
## 👤 7. Contactos

👨‍💻 Autor
Desenvolvido por **Alione Hebo**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/alione-hebo-ab464b2b4/)

[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:alionehebo05@gmail.com)
