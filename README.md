# 🤖 Analisador Inteligente de Currículos com IA Local

Automatize a análise de currículos com uma aplicação de ponta a ponta que combina **OCR**, **LLMs locais** e **verificação de compatibilidade com vagas**.  
Ideal para uso em processos seletivos de RH, de forma **segura, local e sem expor dados sensíveis**.

---

## 🚀 Demonstração

![curriculo-llm-demo](/match_vagas.gif)

---

## 🧰 Tecnologias Utilizadas

| Categoria            | Ferramentas & Bibliotecas                                          |
|----------------------|--------------------------------------------------------------------|
| **LLM Local**        | [Ollama](https://ollama.com) · Modelos: `gemma3:12b`, `gemma3:4b`  |
| **Orquestração**     | LangChain · PromptTemplate                                         |
| **OCR**              | Tesseract OCR                                                      |
| **Conversão PDF**    | Poppler · `pdf2image`                                              |
| **Interface**        | Streamlit                                                          |
| **Similaridade**     | Sentence Transformers (`MiniLM-L6`) + Scikit-learn                |
| **Banco de Dados**   | SQLite                                                             |
| **Backend**          | Python                                                             |

---

## 🧱 Funcionalidades

### 📥 Upload e Leitura de Currículo
- Upload de arquivos PDF
- Conversão para imagem com **Poppler + pdf2image**
- Extração de texto com **Tesseract OCR (pt-BR)**

### 🧠 Extração Estruturada com LLM Local
- Nome, cargo mais recente, experiências, formação, skills, idiomas
- Retorno estruturado em **JSON**
- Prompt especializado para currículos em português

### 🧮 Match com Banco de Vagas
- Similaridade semântica (embedding)
- Filtro automático das **Top 5 vagas mais compatíveis**
- Justificativa da compatibilidade gerada por LLM (com critérios técnicos)

### 🧑‍💼 Gestão de Vagas
- Interface para **criar, editar e excluir vagas**
- Campos como tipo, senioridade, experiência e skills

---

## ⚙️ Instalação

### 1. Instale dependências do sistema

#### 🔠 Tesseract OCR

- **Windows**:  
  [Baixe o instalador da UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)  
  > Marque a opção para adicionar ao PATH

- **Linux**:
  ```bash
  sudo apt install tesseract-ocr
  ```

#### 📄 Poppler (para ler PDFs)

- **Windows**:
  1. Baixe: https://github.com/oschwartz10612/poppler-windows/releases  
  2. Extraia para `C:\poppler\`  
  3. Adicione `C:\poppler\Library\bin` ao PATH  
  4. Reinicie o terminal

- **Linux**:
  ```bash
  sudo apt install poppler-utils
  ```

#### 🤖 Ollama + Modelos

- Instale o Ollama: https://ollama.com  
- Baixe os modelos necessários:

```bash
ollama run gemma3:12b
ollama run gemma3:4b
```

---

### 2. Clone o projeto e instale as dependências Python

```bash
git clone https://github.com/gleissonbispo/match_vagas_llm.git
cd match_vagas_llm
pip install -r requirements.txt
```

---

### 3. Execute o aplicativo

```bash
streamlit run app.py
```

---

## 🔐 Privacidade

Este projeto roda 100% local.  
Nenhum dado de currículo é enviado para servidores externos.  
Ideal para empresas que lidam com dados sensíveis de candidatos.

---
