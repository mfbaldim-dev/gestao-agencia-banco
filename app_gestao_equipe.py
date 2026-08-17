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

# Insira aqui o link exato do seu primeiro aplicativo Streamlit publicado
url_primeiro_app = "https://gestao-agencia-banco-9d3giuxu7ldste3wj5zrp4.streamlit.app/" 

st.sidebar.link_button("📊 Voltar para o Painel Principal", url_primeiro_app, use_container_width=True)
# -----------------------------------------------------------------

# 1. PILARES BSC E VISÃO GERAL
if menu_modulo == "Pilares BSC & Alinhamento":
    st.header("🏛️ Os Pilares da nossa Gestão (BSC 2026)")
    st.info("💡 'O nosso trabalho se sustenta nesses 5 pilares do BSC. Não buscamos apenas o resultado a qualquer custo, mas sim uma gestão comercial estruturada.' — Gerente")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📌 Pilares Estratégicos")
        st.markdown("- **1. Gestão de Pessoas:** Feedbacks frequentes e reconhecimento adequado.")
        st.markdown("- **2. Gestão Comercial:** Planejamento, priorização e metas transformadas em ações.")
        st.markdown("- **3. Atividade Comercial:** Acompanhamento das abordagens e ritmo de conversão.")
        st.markdown("- **4. Gestão de Clientes:** Desenvolvimento e proteção ativa da base.")
        st.markdown("- **5. Gestão de Crédito:** Análise técnica e responsabilidade preventiva.")
        
    with col2:
        st.subheader("🎯 O Grande Momento do Mês")
        st.markdown("- **Balanço da Unidade (Entre os dias 20 e 25):**")
        st.markdown("  - Reunião geral com todo o quadro da agência (08h00 às 09h30).")
        st.markdown("  - Avaliação do fechamento do Orçamento e POBJ do mês anterior.")
        st.markdown("  - Análise de projeções do Portal de Incentivo Variável (SUPERA).")
        st.markdown("  - Celebração pública e premiação das melhores práticas e entregas.")

# 2. RITUAIS SEMANAIS (SEGUNDA A SEXTA)
elif menu_modulo == "Rituais Semanais (Seg a Sex)":
    st.header("📅 Engrenagem da Semana Comercial")
    st.markdown("
