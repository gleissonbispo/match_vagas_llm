import json
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

llm = ChatOllama(model="gemma3:12b")

extract_prompt = PromptTemplate(
    input_variables=["texto"],
    template="""
Você receberá um texto de currículo extraído por OCR.
Extraia as seguintes informações em JSON:
- nome
- cargo_mais_recente
- experiencias (lista)
- formacao (lista)
- skills (lista)
- idiomas (lista)

Retorne **apenas o JSON puro**, sem blocos de código ou explicações.

Currículo:
{texto}
"""
)

def limpar_json_bruto(resposta_llm):
    texto = resposta_llm.strip().replace('json', '')
    if texto.startswith("```"):
        texto = texto.split("```")[1]  # remove bloco inicial
    return texto.strip()

def parse_resume(texto):
    resposta = llm.invoke(extract_prompt.format(texto=texto))
    json_limpo = limpar_json_bruto(resposta.content)
    try:
        return json.loads(json_limpo)
    except json.JSONDecodeError as e:
        print("Erro ao decodificar JSON:", e)
        print("Conteúdo retornado:\n", json_limpo)
        return {}
