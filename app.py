import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Painel de Gestão da Agência", page_icon="📊", layout="wide")

# Inicializar o estado da sessão de forma segura
if "equipe" not in st.session_state:
    st.session_state.equipe = []

st.title("📊 Painel de Gestão do Gerente de Agência")
st.markdown("Acompanhamento de rotinas, crédito, equipe e metas comerciais.")

# Menu lateral
menu = st.sidebar.selectbox("Navegação", [
    "Rotinas Diárias (Checklist)", 
    "Cadastrar Colaborador", 
    "Registrar Produção (FLOG)", 
    "Painel de Alertas e Metas"
], key="menu_navegacao")

# 1. ROTINAS DIÁRIAS
if menu == "Rotinas Diárias (Checklist)":
    st.header("🌅 Checklist de Rotinas Operacionais e Comerciais")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Manhã (08h00 - 09h30)")
        st.checkbox("Acompanhar lista Devedora / Vencidos em Mora", key="c1")
        st.checkbox("Analisar PDD via Microsoft Power BI", key="c2")
        st.checkbox("Verificar PAC e apontamentos no App/WhatsApp", key="c3")
        st.checkbox("Avaliar POBJ Produção linha a linha", key="c4")
        st.checkbox("Oportunidades via CCRE e cross-sell", key="c5")

    with col2:
        st.subheader("Durante o Dia (10h00 - 16h00)")
        st.checkbox("Monitorar ofertas no SMART (Gestão de Contatos)", key="c6")
        st.checkbox("Acompanhar abordagens e material Conversa Boa", key="c7")
        st.checkbox("Realizar ao menos uma visita conjunta com o time", key="c8")

    with col3:
        st.subheader("Fechamento (16h00 - 17h30)")
        st.checkbox("Apurar dados no sistema FLOG", key="c9")
        st.checkbox("Realizar feedbacks e ajustes diários", key="c10")
        st.checkbox("Planejar o próximo dia e prioridades", key="c11")

# 2. CADASTRAR COLABORADOR
elif menu == "Cadastrar Colaborador":
    st.header("👥 Cadastro de Gerentes (Prime / PJ)")
    
    with st.form("form_colaborador", clear_on_submit=True):
        nome = st.text_input("Nome do Gerente")
        segmento = st.selectbox("Segmento", ["Prime", "PJ"])
        meta = st.number_input("Meta atribuída no POBJ (R$)", min_value=0.0, step=1000.0)
        
        submitted = st.form_submit_button("Cadastrar")
        if submitted:
            if nome.strip() != "":
                st.session_state.equipe.append({
                    "nome": nome,
                    "segmento": segmento,
                    "meta": meta,
                    "realizado": 0.0
                })
                st.success(f"Colaborador {nome} cadastrado com sucesso!")
            else:
                st.error("Por favor, preencha o nome do colaborador.")

# 3. REGISTRAR PRODUÇÃO
elif menu == "Registrar Produção (FLOG)":
    st.header("📈 Registro Diário de Produção")
    
    if not st.session_state.equipe:
        st.warning("Nenhum colaborador cadastrado ainda. Vá em 'Cadastrar Colaborador' no menu lateral.")
    else:
        nomes = [c["nome"] for c in st.session_state.equipe]
        colaborador_escolhido = st.selectbox("Selecione o Gerente", nomes, key="select_colab")
        valor_produzido = st.number_input("Valor realizado hoje (R$)", min_value=0.0, step=500.0, key="val_prod")
        
        if st.button("Atualizar Produção"):
            for c in st.session_state.equipe:
                if c["nome"] == colaborador_escolhido:
                    c["realizado"] += valor_produzido
                    st.success(f"Produção de R$ {valor_produzido:,.2f} somada para {colaborador_escolhido}!")

# 4. PAINEL DE ALERTAS E METAS
elif menu == "Painel de Alertas e Metas":
    st.header("📊 Acompanhamento de Metas e Alertas")
    
    st.info("💡 **Lembrete de Gestão de Risco:** Monitorar links de Preventivo de Inadimplência, PDD e carteiras abaixo de 60%.")
    
    if st.session_state.equipe:
        # Criando o DataFrame de forma segura
        df = pd.DataFrame(st.session_state.equipe)
        df["Atingimento (%)"] = (df["realizado"] / df["meta"]) * 100
        df["Atingimento (%)"] = df["Atingimento (%)"].fillna(0).round(1)
        
        # Exibir tabela formatada
        st.dataframe(df, use_container_width=True)
        
        # Gráfico seguro usando st.bar_chart com índice limpo
        st.subheader("Progresso por Gerente")
        df_chart = df.set_index("nome")[["realizado", "meta"]]
        st.bar_chart(df_chart)
    else:
        st.warning("Sem dados de equipe cadastrados no momento.")
