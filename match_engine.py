from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from langchain_ollama import ChatOllama
import sqlite3

model = SentenceTransformer('all-MiniLM-L6-v2')
llm = ChatOllama(model="gemma3:4b")

def match_resume_to_jobs(cv_text):
    conn = sqlite3.connect("data/vagas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, titulo, descricao FROM vagas")
    vagas = cursor.fetchall()
    conn.close()

    cv_emb = model.encode([cv_text])[0]

    # Calcula similaridade para todas as vagas
    resultados_simples = []
    for vid, titulo, desc in vagas:
        vaga_emb = model.encode([desc])[0]
        sim = cosine_similarity([cv_emb], [vaga_emb])[0][0]
        resultados_simples.append((vid, titulo, desc, sim))

    # Ordena e pega Top 5
    top5 = sorted(resultados_simples, key=lambda x: x[3], reverse=True)[:5]

    # Chama o LLM só para essas 5 vagas
    resultados_finais = []
    for _, titulo, desc, score in top5:
        prompt = fprompt = f"""
**Análise de Compatibilidade entre Currículo e Vaga**

**Currículo Analisado:**
{cv_text}

**Descrição da Vaga:**
{desc}

**Instruções para Análise:**
1. Identifique os requisitos ESSENCIAIS da vaga (hard skills, qualificações, experiências obrigatórias)
2. Identifique os requisitos DESEJÁVEIS da vaga (soft skills, diferenciais)
3. Analise o currículo destacando correspondências explícitas e implícitas
4. Considere equivalências (ex: formação similar, experiências transferíveis)
5. Atribua pesos diferentes para requisitos essenciais vs desejáveis
6. Use escala conservadora (0-100) onde 100 só se todos critérios essenciais forem totalmente atendidos
7. A analise precisa ser extremante conservadora e embasada

**Critérios de Avaliação:**
- Correspondência de Habilidades Técnicas (0-20 pontos)
- Adequação da Experiência Profissional (0-20 pontos)
- Compatibilidade Educacional/Certificações (0-10 pontos)
- Soft Skills e Fit Cultural (0-10 pontos)
- Expertise geral compativel (0-40 pontos)

**Formato de Resposta Exigido:**
- Score: [0-100]
- Breve Justificativa em um paragrafo.

**Importante:**
- Se houver ambiguidade, priorize análise conservadora
- Destaque casos onde experiências podem compensar requisitos
- Considere sinônimos e variações terminológicas
- Mantenha resposta em português brasileiro
"""
        resposta = llm.invoke(prompt)
        resultados_finais.append((titulo, score, resposta.content.strip()))

    return resultados_finais
