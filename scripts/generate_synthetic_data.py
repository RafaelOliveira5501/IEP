# scripts/generate_synthetic_data.py (crie em scripts/)
import pandas as pd
import random
import os

os.makedirs("data/processed", exist_ok=True)

n = 300
rows = []
for i in range(n):
    idade = random.choice([6,7,8,9,10,11])
    nivel_leitura = random.choices(["iniciante","basico","intermediario"], [0.5,0.35,0.15])[0]
    nivel_matematica = random.choices(["iniciante","basico","intermediario"], [0.5,0.35,0.15])[0]
    atencao = random.choices(["baixa","media","alta"], [0.4,0.45,0.15])[0]
    interesse_imagem = random.choice([0,1])
    interesse_numeros = random.choice([0,1])
    interesse_jogos = random.choice([0,1])

    # regras para criar labels sintéticas (simples)
    metodo_atividades_curtas = 1 if atencao == "baixa" or idade <= 7 else 0
    metodo_usar_imagens = 1 if interesse_imagem or nivel_leitura == "iniciante" else 0
    metodo_jogos_educativos = 1 if interesse_jogos else 0
    desafio_leitura = 1 if nivel_leitura == "iniciante" else 0
    desafio_atencao = 1 if atencao == "baixa" else 0

    rows.append({
        "idade": idade,
        "nivel_leitura": nivel_leitura,
        "nivel_matematica": nivel_matematica,
        "atencao": atencao,
        "interesse_imagem": interesse_imagem,
        "interesse_numeros": interesse_numeros,
        "interesse_jogos": interesse_jogos,
        "metodo_atividades_curtas": metodo_atividades_curtas,
        "metodo_usar_imagens": metodo_usar_imagens,
        "metodo_jogos_educativos": metodo_jogos_educativos,
        "desafio_leitura": desafio_leitura,
        "desafio_atencao": desafio_atencao,
    })

df = pd.DataFrame(rows)
df.to_csv("data/processed/alunos_clean.csv", index=False)
print("CSV gerado em data/processed/alunos_clean.csv")
