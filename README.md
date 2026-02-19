Gen AI Cold Email Generator — README

A step-by-step README for a cold email generator using Llama 3.1, LangChain, and ChromaDB.
Important: If you (or other contributors) try to use a Gradio interface while developing in PyCharm or VS Code, prefer Streamlit instead — Streamlit integrates more reliably with local IDE workflows (run via streamlit run) and works well from notebooks, terminals, and CI.

Table of contents

Overview

Features

Tech stack

Prerequisites

Quick setup (step-by-step)

Run the Jupyter notebook (VS Code / PyCharm)

Run the Streamlit UI (recommended for IDEs)

Converting Gradio -> Streamlit (if repo contains Gradio)

Example ingest and RAG flow

Environment variables / .env example

Troubleshooting & tips

Contributing & License

Overview

This repo builds a personalized cold email generator using retrieval-augmented generation (RAG). ChromaDB stores company/job/lead vectors, LangChain orchestrates retrieval + prompt templates, and Llama 3.1 generates the email drafts.

Features

Context-aware cold emails from job descriptions or lead profiles

RAG (ChromaDB) for retrieving personalized content snippets

LangChain pipelines for prompt + retrieval orchestration

Streamlit UI for easy local development & demos (recommended)

Example Jupyter notebook for experiments

Tech stack

Python 3.8+

LangChain

ChromaDB

Llama 3.1 (via your chosen runtime/provider — local weights, API, or adapter)

Streamlit (UI recommended for PyCharm & VS Code)

Optional: Jupyter / .ipynb notebook for exploration

Prerequisites

Git, Python 3.8+

Access to Llama 3.1 (local runtime or hosted API) — ensure you have necessary model files or API credentials.

(Optional) Docker if you prefer containerized runs.

Quick setup (step-by-step)

Clone
cd gen-ai-cold-email


Create venv & activate
Linux / macOS:

python -m venv venv
source venv/bin/activate


Windows:

python -m venv venv
venv\Scripts\activate


Install dependencies
Create requirements.txt or use the repo one:

pip install -r requirements.txt


Minimal deps (example):

langchain
chromadb
streamlit
jupyter
python-dotenv
transformers   # only if you're using a HF-like interface
sentence_transformers


Prepare .env (see example below)

Ingest documents into Chroma
(Place leads/job descriptions as .csv or .md and run ingestion)

python scripts/ingest.py --source data/leads.csv --persist_dir ./chroma_db


Run Streamlit UI (recommended)

streamlit run app.py


Or run the notebook (for experiments)

jupyter notebook notebooks/Gen_AI_Cold_email_generator.ipynb

Run the Jupyter notebook (VS Code / PyCharm)
VS Code

Install VS Code extensions: Python and Jupyter.

Ensure the selected kernel matches your virtualenv (bottom-right kernel selector).

Open notebooks/Gen_AI_Cold_email_generator.ipynb and run cells.

PyCharm

PyCharm Professional: open .ipynb directly and use built-in notebook support.

PyCharm Community: run a local Jupyter server:

jupyter notebook
# open the URL shown in your browser to access the notebook


Note: If using PyCharm or VS Code for running an app UI, use Streamlit (see next section) instead of Gradio for smoother local development.

Run the Streamlit UI (recommended for IDEs)

Streamlit is recommended when developing in PyCharm/VS Code because:

easy streamlit run app.py workflow

live reload on file save

works well in terminals integrated into IDEs

Install & run

pip install streamlit
streamlit run app.py


Minimal app.py example

import streamlit as st
from langchain import LLMChain, PromptTemplate
# configure your Llama 3.1 LLM wrapper here
# configure chromadb client and retriever here

st.title("Gen AI Cold Email Generator")
job_desc = st.text_area("Paste job/lead description")
if st.button("Generate Email"):
    # 1) retrieve relevant context from Chroma
    # 2) call Llama 3.1 via LangChain LLM wrapper
    # 3) display result
    st.code("Generated email goes here")

Converting Gradio -> Streamlit (if repo contains Gradio)

If your repo has an existing Gradio interface, prefer converting to Streamlit when running locally in PyCharm or VS Code. Gradio sometimes opens a separate tab with background threading that can be awkward inside IDEs and notebooks.

Gradio example (old):

import gradio as gr

def gen_email(text):
    return llm_chain.run(text)

gr.Interface(fn=gen_email, inputs="text", outputs="text").launch()


Equivalent Streamlit (recommended):

import streamlit as st

def gen_email(text):
    return llm_chain.run(text)

st.text_area("Job/lead", key="job")
if st.button("Generate"):
    st.write(gen_email(st.session_state.job))


Why Streamlit?

single command streamlit run app.py

live reload and debug-friendly in IDE terminals

easier to embed rich components, files & downloads

Example ingest & RAG flow

Embedding: use a sentence-transformers model (or your embedding endpoint) to embed job/lead text.

Persist: store vectors & metadata in ChromaDB.

Retriever: LangChain retriever queries Chroma to return top-k context chunks.

Prompt: templates + retrieved context feed Llama 3.1 via LangChain to generate final email.

Example CLI:

python scripts/ingest.py --source data/leads.csv --persist_dir ./chroma_db
python scripts/query_and_generate.py --query "Senior backend engineer at Acme" 

Environment variables / .env example

Create a .env in repo root:

LLAMA_API_URL=https://your-llama-provider.example
LLAMA_API_KEY=your_llama_api_key_here
CHROMA_PERSIST_DIR=./chroma_db
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
STREAMLIT_PORT=8501


Important: Configure Llama 3.1 per your access method — local weights, HF endpoint, or commercial API. Replace placeholders accordingly.

Troubleshooting & tips

Llama access: Llama 3.1 can require specific runtimes. If using local weights, ensure you have enough RAM/GPU and the correct runtime (transformers/vllm/llama.cpp adapters).

Chroma persistence: if you see no results, confirm persist_dir paths match between ingestion and runtime.

Kernel mismatch: in VS Code, pick the interpreter matching your virtualenv.

Gradio odd behavior in IDEs: prefer Streamlit locally — see conversion section above.

Notebook to script:

jupyter nbconvert --to script notebooks/Gen_AI_Cold_email_generator.ipynb -o scripts/notebook_to_script.py


Then adapt to Streamlit or a runnable CLI.

Contributing

PRs welcome — add issues for feature requests or bugs. Please include:

steps to reproduce

Python version & OS

minimal code or data sample

License

Add your preferred license (e.g., MIT). Example LICENSE file recommended.

Final notes (important)

Streamlit is recommended for local development in PyCharm & VS Code. If you see a Gradio UI in the repo, convert to Streamlit for more predictable IDE behavior.

When integrating Llama 3.1, follow the model provider’s license and distribution rules. Replace placeholders in .env with your real credentials.

