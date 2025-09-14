# frontend/app.py
import streamlit as st
import requests
import os

API_URL = os.getenv("API_URL", "http://localhost:8000")

st.set_page_config(page_title="PEI - Insights", layout="centered")

st.title("PEI - Gerador de Insights (MVP)")

with st.form("aluno_form"):
    nome = st.text_input("Nome (opcional)")
    idade = st.number_input("Idade", min_value=4, max_value=18, value=8)
    nivel_leitura = st.selectbox("Nível de leitura", ["iniciante", "basico", "intermediario"])
    nivel_matematica = st.selectbox("Nível de matemática", ["iniciante", "basico", "intermediario"])
    atencao = st.selectbox("Atenção", ["baixa", "media", "alta"])
    interesse_imagem = st.checkbox("Gosta de imagens?")
    interesse_numeros = st.checkbox("Gosta de números?")
    interesse_jogos = st.checkbox("Gosta de jogos?")
    submitted = st.form_submit_button("Gerar insights")

if submitted:
    # Primeiro, cria aluno via DB: para simplicidade, pedimos que a API já tenha endpoint para criar aluno.
    # Se não implementou, você pode inserir manualmente um aluno no DB e usar o id — aqui vamos supor que existe POST /aluno.
    payload = {
        "nome": nome,
        "idade": idade,
        "nivel_leitura": nivel_leitura,
        "nivel_matematica": nivel_matematica,
        "atencao": atencao,
        "interesse_imagem": interesse_imagem,
        "interesse_numeros": interesse_numeros,
        "interesse_jogos": interesse_jogos
    }

    # Tentar criar aluno
    r = requests.post(f"{API_URL}/aluno", json=payload)
    if r.status_code == 201:
        aluno = r.json()
        aluno_id = aluno["id"]
    else:
        # fallback: assume endpoint não existe — criar um aluno temporário via /insights/generate (precisa do id)
        st.error("Não foi possível criar aluno via API. Implemente POST /aluno ou use DB manualmente.")
        st.stop()

    # Gerar insights
    r2 = requests.post(f"{API_URL}/insights/generate/{aluno_id}")
    if r2.status_code == 200:
        ins = r2.json()
        st.success("Insights gerados:")
        st.write(ins)
        # Exibir em cards simples
        st.subheader("Forças")
        for f in ins.get("forcas", []):
            st.write(f"- {f}")
        st.subheader("Desafios")
        for d in ins.get("desafios", []):
            st.write(f"- {d}")
        st.subheader("Métodos recomendados")
        for m in ins.get("metodos_recomendados", []):
            st.write(f"- {m}")
    else:
        st.error("Erro ao gerar insights: " + r2.text)
