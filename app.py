import streamlit as st
from db import init_db, popular_db, listar_vagas, adicionar_vaga, editar_vaga, excluir_vaga
from ocr_extract import extract_text_from_pdf
from resume_parser import parse_resume
from match_engine import match_resume_to_jobs

# Inicializa o banco de dados
init_db()
popular_db()

# Páginas
pagina = st.sidebar.radio("Navegar", ["📄 Analisar Currículo", "🔧 Gerenciar Vagas"])

if pagina == "📄 Analisar Currículo":
    st.title("📄 Analisador de Currículos com IA Local")

    cv_file = st.file_uploader("Envie um currículo em PDF", type=["pdf"])
    if cv_file:
        with st.spinner("🔍 Realizando OCR do currículo..."):
            texto = extract_text_from_pdf(cv_file.read())

        with st.expander("📜 Texto extraído"):
            st.write(texto[:1000] + "...")

        with st.spinner("📑 Extraindo informações estruturadas com LLM..."):
            dados = parse_resume(texto)

        with st.expander("📊 Dados estruturados do currículo"):
            st.json(dados)

        with st.spinner("⚖️ Calculando similaridade com as vagas..."):
            resultados = match_resume_to_jobs(texto)

        st.success("✅ Análise concluída!")

        st.markdown("### 🎯 Top 5 Vagas Mais Compatíveis")
        for titulo, score, justificativa in resultados:
            st.markdown(f"**{titulo}** — Similaridade: `{round(score*100)}%`")
            st.caption(justificativa)
            st.markdown("---")

elif pagina == "🔧 Gerenciar Vagas":
    st.title("🔧 Gerenciador de Vagas")

    with st.expander("➕ Adicionar nova vaga"):
        with st.form("form_nova_vaga"):
            titulo = st.text_input("Título da vaga")
            descricao = st.text_area("Descrição")
            tipo = st.selectbox("Tipo", ["tecnica", "gerencial", "comportamental"])
            skills = st.text_input("Skills requeridas (separadas por vírgula)")
            experiencia = st.text_input("Experiência mínima")
            senioridade = st.text_input("Senioridade (Júnior, Pleno, Sênior)")
            submitted = st.form_submit_button("Salvar")
            if submitted:
                adicionar_vaga(titulo, descricao, tipo, skills, experiencia, senioridade)
                st.success("✅ Vaga adicionada!")

    st.markdown("### 📋 Vagas Cadastradas")
    vagas = listar_vagas()
    for v in vagas:
        with st.expander(f"🔹 {v[1]}"):
            with st.form(f"edit_{v[0]}"):
                titulo = st.text_input("Título", value=v[1], key=f"t{v[0]}")
                descricao = st.text_area("Descrição", value=v[2], key=f"d{v[0]}")
                tipo = st.selectbox("Tipo", ["tecnica", "gerencial", "comportamental"], index=["tecnica", "gerencial", "comportamental"].index(v[3]), key=f"tp{v[0]}")
                skills = st.text_input("Skills", value=v[4], key=f"s{v[0]}")
                experiencia = st.text_input("Experiência mínima", value=v[5], key=f"e{v[0]}")
                senioridade = st.text_input("Senioridade", value=v[6], key=f"sr{v[0]}")
                col1, col2 = st.columns([1,1])
                with col1:
                    if st.form_submit_button("💾 Salvar alterações"):
                        editar_vaga(v[0], titulo, descricao, tipo, skills, experiencia, senioridade)
                        st.success("✅ Vaga atualizada.")
                with col2:
                    if st.form_submit_button("🗑️ Excluir vaga"):
                        excluir_vaga(v[0])
                        st.warning("❌ Vaga excluída.")
