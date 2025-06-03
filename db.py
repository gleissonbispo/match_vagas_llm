import sqlite3

def init_db():
    conn = sqlite3.connect("data/vagas.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vagas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            descricao TEXT,
            tipo TEXT,
            skills_requeridas TEXT,
            experiencia_min TEXT,
            senioridade TEXT
        )
    """)
    conn.commit()
    conn.close()

def popular_db():
    conn = sqlite3.connect("data/vagas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM vagas")
    if cursor.fetchone()[0] == 0:
        vagas = [
            ("Desenvolvedor Backend", "Desenvolvimento de APIs em Python e Node.js", "tecnica", "Python, Node.js, REST", "3 anos", "Pleno"),
            ("Desenvolvedor Frontend", "Criação de interfaces com React e Vue", "tecnica", "React, Vue, JavaScript", "2 anos", "Pleno"),
            ("Analista de Dados", "Análise de dados com SQL, Power BI e Python", "tecnica", "SQL, Power BI, Python", "2 anos", "Pleno"),
            ("Engenheiro de Dados", "Construção de pipelines com Spark e Airflow", "tecnica", "Spark, Airflow, ETL", "3 anos", "Sênior"),
            ("Cientista de Dados", "Modelagem preditiva e análise estatística", "tecnica", "Python, Machine Learning, Estatística", "3 anos", "Sênior"),
            ("DevOps Engineer", "Integração e entrega contínua com Docker e Kubernetes", "tecnica", "CI/CD, Docker, Kubernetes", "3 anos", "Sênior"),
            ("Tech Lead", "Liderança técnica e revisão de código", "gerencial", "Arquitetura, Git, Mentoria", "5 anos", "Sênior"),
            ("QA Engineer", "Testes automatizados de software", "tecnica", "Selenium, Cypress, TDD", "2 anos", "Pleno"),
            ("Product Manager", "Gestão de roadmap e backlog", "gerencial", "Scrum, Produto, Análise", "4 anos", "Sênior"),
            ("UX Designer", "Prototipação e testes de usabilidade", "comportamental", "Figma, UX Research", "2 anos", "Pleno"),
            ("Analista de Marketing Digital", "Planejamento e execução de campanhas", "tecnica", "Google Ads, Meta Ads, SEO", "2 anos", "Pleno"),
            ("Social Media", "Gestão de redes sociais e conteúdo", "comportamental", "Instagram, TikTok, Redação", "1 ano", "Júnior"),
            ("Copywriter", "Criação de textos persuasivos para campanhas", "tecnica", "Copywriting, Funil de Vendas", "2 anos", "Pleno"),
            ("Designer Gráfico", "Criação de peças para redes sociais e anúncios", "tecnica", "Photoshop, Illustrator", "1 ano", "Júnior"),
            ("Coordenador de Marketing", "Gestão de equipe e estratégias digitais", "gerencial", "Liderança, Mídia Paga, SEO", "4 anos", "Sênior"),
            ("Growth Hacker", "Experimentação e escalabilidade de produtos", "tecnica", "Testes A/B, Métricas, Produto", "3 anos", "Pleno"),
            ("Analista de CRM", "Gestão de relacionamento com clientes via e-mail e SMS", "tecnica", "RD Station, Automação", "2 anos", "Pleno"),
            ("Especialista em SEO", "Otimização de conteúdo e estrutura de sites", "tecnica", "SEO, Analytics, Semrush", "3 anos", "Sênior"),
            ("Gerente de Produto de Marketing", "Integração entre produto e estratégia de marketing", "gerencial", "Produto, Estratégia, Comunicação", "5 anos", "Sênior"),
            ("Videomaker", "Produção e edição de vídeos para campanhas", "tecnica", "Premiere, After Effects", "2 anos", "Pleno"),
            ("Business Partner", "Atuação estratégica junto a áreas de negócio", "gerencial", "Consultoria Interna, Clima, Indicadores", "4 anos", "Sênior"),
            ("Analista de Recrutamento e Seleção", "Condução de processos seletivos", "tecnica", "Entrevistas, Hunting, Vagas Tech", "2 anos", "Pleno"),
            ("Especialista em Remuneração", "Desenho de política salarial e PPR", "tecnica", "Cargos e Salários, PLR, Benchmarking", "3 anos", "Sênior"),
            ("Analista de Clima Organizacional", "Pesquisas e ações de clima", "comportamental", "Engajamento, Comunicação Interna", "2 anos", "Pleno"),
            ("Coordenador de Desenvolvimento", "Gestão de trilhas de aprendizado", "gerencial", "Liderança, LNT, Educação Corporativa", "4 anos", "Sênior"),
            ("Analista de People Analytics", "Análises preditivas e modelagens de turnover", "tecnica", "Python, Power BI, SQL", "3 anos", "Pleno"),
            ("Assistente de RH", "Rotinas de RH e apoio administrativo", "comportamental", "Organização, Atendimento", "1 ano", "Júnior"),
            ("Gerente de RH", "Gestão de todas as frentes de RH", "gerencial", "Liderança, Cultura, Indicadores", "6 anos", "Sênior"),
            ("Analista de Treinamento", "Organização de treinamentos e avaliações", "comportamental", "Andragogia, Feedback, Avaliação", "2 anos", "Pleno"),
            ("Especialista em Cultura", "Promoção e monitoramento de cultura organizacional", "comportamental", "Cultura, Missão, Valores", "3 anos", "Sênior")
        ]
        cursor.executemany("""
            INSERT INTO vagas (titulo, descricao, tipo, skills_requeridas, experiencia_min, senioridade)
            VALUES (?, ?, ?, ?, ?, ?)
        """, vagas)
    conn.commit()
    conn.close()

def adicionar_vaga(titulo, descricao, tipo, skills, experiencia, senioridade):
    conn = sqlite3.connect("data/vagas.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO vagas (titulo, descricao, tipo, skills_requeridas, experiencia_min, senioridade)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (titulo, descricao, tipo, skills, experiencia, senioridade))
    conn.commit()
    conn.close()

def listar_vagas():
    conn = sqlite3.connect("data/vagas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vagas")
    vagas = cursor.fetchall()
    conn.close()
    return vagas

def editar_vaga(id, titulo, descricao, tipo, skills, experiencia, senioridade):
    conn = sqlite3.connect("data/vagas.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE vagas
        SET titulo=?, descricao=?, tipo=?, skills_requeridas=?, experiencia_min=?, senioridade=?
        WHERE id=?
    """, (titulo, descricao, tipo, skills, experiencia, senioridade, id))
    conn.commit()
    conn.close()

def excluir_vaga(id):
    conn = sqlite3.connect("data/vagas.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM vagas WHERE id=?", (id,))
    conn.commit()
    conn.close()
