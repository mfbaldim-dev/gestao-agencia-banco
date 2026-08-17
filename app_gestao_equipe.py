import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Método Comercial - Rotina Inegociável", page_icon="🎯", layout="wide")

# Inicializar o estado da sessão para rituais e acompanhamentos da equipe
if "rituais_equipe" not in st.session_state:
    st.session_state.rituais_equipe = []

if "feedbacks_lista" not in st.session_state:
    st.session_state.feedbacks_lista = []

st.title("🎯 Gestão Comercial: Rotina Inegociável e Pilares BSC")
st.markdown("Módulo complementar focado nos rituais semanais de performance, pilares do BSC e alinhamento com a equipe.")

# Menu lateral para navegação interna deste novo módulo
menu_modulo = st.sidebar.selectbox("Módulos da Gestão da Equipe", [
    "Pilares BSC & Alinhamento",
    "Rituais Semanais (Seg a Sex)",
    "Registro de Feedbacks e Alinhamentos",
    "Painel de Acompanhamento"
], key="menu_mod_equipe")

# --- ATALHO PARA VOLTAR AO PRIMEIRO APLICATIVO NA BARRA LATERAL ---
st.sidebar.divider()
st.sidebar.markdown("### 🔗 Navegação Geral")

# Insira aqui o link do seu primeiro aplicativo Streamlit publicado
url_primeiro_app = "https://seu-primeiro-app.streamlit.app" 

st.sidebar.link_button("📊 Voltar para o Painel Principal", url_primeiro_app, use_container_width=True)
# -----------------------------------------------------------------

# 1. PILARES BSC E VISÃO GERAL
if menu_modulo == "Pilares BSC & Alinhamento":
    st.header("🏛️ Os Pilares da nossa Gestão (BSC 2026)")
    st.info("💡 *'O nosso trabalho se sustenta nesses 5 pilares do BSC. Não buscamos apenas o resultado a qualquer custo, mas sim uma gestão comercial estruturada.'* — Gerente")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📌 Pilares Estratégicos")
        st.markdown("""
        * **1. Gestão de Pessoas:** Feedbacks frequentes e reconhecimento adequado.
        * **2. Gestão Comercial:** Planejamento, priorização e metas transformadas em ações.
        * **3. Atividade Comercial:** Acompanhamento das abordagens e ritmo de conversão.
        * **4. Gestão de Clientes:** Desenvolvimento e proteção ativa da base.
        * **5. Gestão de Crédito:** Análise técnica e responsabilidade preventiva.
        """)
        
    with col2:
        st.subheader("🎯 O Grande Momento do Mês")
        st.markdown("""
        * **Balanço da Unidade (Entre os dias 20 e 25):**
          * Reunião geral com todo o quadro da agência (08h00 às 09h30).
          * Avaliação do fechamento do Orçamento e POBJ do mês anterior.
          * Análise de projeções do Portal de Incentivo Variável (SUPERA).
          * Celebração pública e premiação das melhores práticas e entregas.
        """)

# 2. RITUAIS SEMANAIS (SEGUNDA A SEXTA)
elif menu_modulo == "Rituais Semanais (Seg a Sex)":
    st.header("📅 Engrenagem da Semana Comercial")
    st.markdown("Acompanhe o foco e o ritual de cada dia da semana para garantir previsibilidade de resultados.")
    
    dia_selecionado = st.selectbox("Selecione o Dia da Semana para Detalhar", [
        "Segunda-feira: Alinhamento e Alocação",
        "Terça-feira: Capacitação (Circuito do Saber)",
        "Quarta-feira: Diagnóstico de Carteira (PADE)",
        "Quinta-feira: Gestão da Base (80/20)",
        "Sexta-feira: Prestação de Contas e Apuração"
    ], key="select_dia_semana")
    
    if "Segunda" in dia_selecionado:
        st.subheader("📌 Segunda-feira: Alinhamento e Alocação")
        st.markdown("""
        * **Cascateamento DR/GR:** Reunião conjunta e presencial com 100% da equipe (ou remota para PAs/PABs).
        * **Rodada da Produtividade:** Distribuição
