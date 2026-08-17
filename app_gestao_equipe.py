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

# --- ATALHO PARA O SEGUNDO APLICATIVO NA BARRA LATERAL ---
st.sidebar.divider()
st.sidebar.markdown("### 🔗 Módulos Complementares")
# Substitua o link abaixo pelo link real do seu segundo app publicado no Streamlit Cloud
st.sidebar.page_link("https://gestao-agencia-banco-9d3giuxu7ldste3wj5zrp4.streamlit.app/", label="Ir para Gestão da Agencia", icon="🎯")
# --------------------------------------------------------

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
        * **Rodada da Produtividade:** Distribuição dos objetivos semanais respeitando a referência de **25% da meta do mês**.
        * *Foco:* Ler o contexto estratégico e definir prioridades nas listas de Alerta 1 e Melhores Ofertas.
        """)
    elif "Terça" in dia_selecionado:
        st.subheader("🧠 Terça-feira: Capacitação (Circuito do Saber)")
        st.markdown("""
        * **Formato:** Realização de aula prática de 30 minutos, 30 minutos antes do expediente.
        * **Ambiente:** Organização em formato de "U" com sinalização de treinamento.
        * *Foco:* Condução pessoal pelo gerente, propondo desafios práticos imediatos e preenchimento de quizzes.
        """)
    elif "Quarta" in dia_selecionado:
        st.subheader("👤 Quarta-feira: Diagnóstico de Carteira")
        st.markdown("""
        * **Atendimento Individual:** Sessões com foco em gerentes com desempenho abaixo de 60% no PADE.
        * **Indicadores:** Análise de RO/ROB e alinhamento com a cultura do SUPERA.
        * *Foco:* Mapear o potencial não explorado e mitigar o acúmulo de gaps.
        """)
    elif "Quinta" in dia_selecionado:
        st.subheader("👥 Quinta-feira: Gestão da Base")
        st.markdown("""
        * **Análise Estruturada:** Estudo de entradas, saídas e inativações de contas.
        * **Atuação Focal:** Aplicação da regra 80/20 em clientes estratégicos, maiores investidores e controle rigoroso dos maiores riscos.
        """)
    elif "Sexta" in dia_selecionado:
        st.subheader("📊 Sexta-feira: Prestação de Contas")
        st.markdown("""
        * **Apuração:** Rodada da Produtividade comparando o planejado versus o realizado de cada Gerente Prime e PJ.
        * *Foco:* Investigar dispersões, aplicar correções de rota e consolidar os resultados da semana.
        """)

# 3. REGISTRO DE FEEDBACKS E ALINHAMENTOS
elif menu_modulo == "Registro de Feedbacks e Alinhamentos":
    st.header("📝 Registro de Feedbacks e Planos de Ação Diários")
    st.markdown("Utilize este espaço para registrar os alinhamentos rápidos feitos após o fechamento do FLOG ou durante as sessões de quarta-feira.")
    
    with st.form("form_feedback", clear_on_submit=True):
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            colaborador_fb = st.text_input("Nome do Colaborador")
        with col_f2:
            tipo_sessao = st.selectbox("Tipo de Alinhamento", ["Feedback Diário (FLOG)", "Diagnóstico de Carteira (Quarta-feira)", "Revisão de Metas"])
            
        ponto_atencao = st.text_area("Ponto de Atenção / Desvio Mapeado")
        combinado = st.text_area("Combinado / Plano de Ação Prático")
        
        btn_salvar_fb = st.form_submit_button("Registrar Alinhamento")
        if btn_salvar_fb:
            if colaborador_fb.strip() != "":
                st.session_state.feedbacks_lista.append({
                    "colaborador": colaborador_fb,
                    "tipo": tipo_sessao,
                    "atencao": ponto_atencao,
                    "combinado": combinado
                })
                st.success(f"Feedback para {colaborador_fb} registrado com sucesso!")
            else:
                st.error("Por favor, informe o nome do colaborador.")

# 4. PAINEL DE ACOMPANHAMENTO DE REGISTROS
elif menu_modulo == "Painel de Acompanhamento":
    st.header("📈 Histórico de Registros e Alinhamentos da Equipe")
    
    if st.session_state.feedbacks_lista:
        df_fb = pd.DataFrame(st.session_state.feedbacks_lista)
        st.dataframe(df_fb, use_container_width=True)
        
        if st.button("🗑️ Limpar Histórico de Registros"):
            st.session_state.feedbacks_lista = []
            st.rerun()
    else:
        st.info("Nenhum feedback ou alinhamento registrado até o momento.")
