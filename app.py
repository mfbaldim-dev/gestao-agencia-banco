import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Painel de Gestão da Agência", page_icon="📊", layout="wide")

# Inicializar o estado da sessão de forma segura
if "equipe" not in st.session_state:
    st.session_state.equipe = []

if "temp_produtos" not in st.session_state:
    st.session_state.temp_produtos = []

st.title("📊 Painel de Gestão do Gerente de Agência")
st.markdown("Acompanhamento de rotinas, crédito, equipe e metas comerciais.")

# Menu lateral principal
menu = st.sidebar.selectbox("Navegação Principal", [
    "Rotinas Diárias (Checklist)", 
    "Cadastrar Colaborador", 
    "Registrar Produção (FLOG)", 
    "Painel de Alertas e Metas"
], key="menu_navegacao")

# --- ATALHO PARA O SEGUNDO APLICATIVO NA BARRA LATERAL ---
st.sidebar.divider()
st.sidebar.markdown("### 🔗 Módulos Complementares")
# Substitua o link abaixo pelo link real do seu segundo app publicado no Streamlit Cloud
st.sidebar.page_link("https://seu-segundo-app.streamlit.app", label="Ir para Gestão da Equipe (Rotina Inegociável)", icon="🎯")
# --------------------------------------------------------

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

# 2. CADASTRAR COLABORADOR E PRODUTOS
elif menu == "Cadastrar Colaborador":
    st.header("👥 Cadastro de Gerentes e Metas por Produto")
    
    nome = st.text_input("Nome do Gerente", key="input_nome_gerente")
    segmento = st.selectbox("Segmento", ["Prime", "PJ"], key="select_segmento_gerente")
    
    st.divider()
    st.subheader("📦 Composição de Produtos e Metas")
    
    col_p1, col_p2, col_p3 = st.columns([2, 2, 1])
    with col_p1:
        produto_nome = st.text_input("Nome do Produto (ex: Crédito PJ, Seguros)", key="input_nome_prod")
    with col_p2:
        produto_meta = st.number_input("Meta do Produto (R$)", min_value=0.0, step=500.0, key="input_meta_prod")
    with col_p3:
        st.write("") 
        st.write("")
        btn_add_produto = st.button("➕ Adicionar Produto")
        
    if btn_add_produto:
        if produto_nome.strip() != "":
            st.session_state.temp_produtos.append({
                "produto": produto_nome,
                "meta_produto": produto_meta
            })
            st.success(f"Produto '{produto_nome}' adicionado à lista!")
        else:
            st.warning("Informe o nome do produto antes de adicionar.")
            
    if st.session_state.temp_produtos:
        st.markdown("**Produtos já inseridos para este gerente:**")
        df_temp = pd.DataFrame(st.session_state.temp_produtos)
        st.dataframe(df_temp, use_container_width=True)
        
        if st.button("🗑️ Limpar Lista de Produtos"):
            st.session_state.temp_produtos = []
            st.rerun()
    
    st.divider()
    
    if st.button("💾 Cadastrar Gerente Completo", type="primary"):
        if nome.strip() == "":
            st.error("Por favor, preencha o nome do colaborador.")
        elif not st.session_state.temp_produtos:
            st.error("Adicione pelo menos um produto e meta antes de finalizar o cadastro.")
        else:
            meta_total = sum([p["meta_produto"] for p in st.session_state.temp_produtos])
            
            st.session_state.equipe.append({
                "nome": nome,
                "segmento": segmento,
                "meta": meta_total,
                "realizado": 0.0,
                "produtos": st.session_state.temp_produtos.copy()
            })
            
            st.session_state.temp_produtos = []
            st.success(f"Gerente {nome} cadastrado com sucesso com meta total de R$ {meta_total:,.2f}!")

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
        df = pd.DataFrame([{
            "nome": c["nome"],
            "segmento": c["segmento"],
            "meta": c["meta"],
            "realizado": c["realizado"]
        } for c in st.session_state.equipe])
        
        df["Atingimento (%)"] = (df["realizado"] / df["meta"]) * 100
        df["Atingimento (%)"] = df["Atingimento (%)"].fillna(0).round(1)
        
        st.subheader("Resumo da Equipe")
        st.dataframe(df, use_container_width=True)
        
        st.subheader("Detalhamento de Metas por Produto")
        for c in st.session_state.equipe:
            with st.expander(f"Gerente: {c['nome']} ({c['segmento']})"):
                if "produtos" in c and c["produtos"]:
                    df_prod = pd.DataFrame(c["produtos"])
                    st.dataframe(df_prod, use_container_width=True)
                else:
                    st.write("Nenhum produto detalhado cadastrado.")
        
        st.subheader("Progresso Geral por Gerente")
        df_chart = df.set_index("nome")[["realizado", "meta"]]
        st.bar_chart(df_chart)
    else:
        st.warning("Sem dados de equipe cadastrados no momento.")
