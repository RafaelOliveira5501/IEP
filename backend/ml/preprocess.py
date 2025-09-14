# backend/ml/preprocess.py
# transforma dict de features em vetor numérico (ordenação simples)
def encode_features(d):
    # mapeamentos simples - mantenha consistentes entre treino/serving
    map_nivel = {"iniciante":0, "basico":1, "intermediario":2}
    map_atencao = {"baixa":0, "media":1, "alta":2}

    return [
        int(d.get("idade", 0)),
        map_nivel.get(d.get("nivel_leitura", "iniciante"), 0),
        map_nivel.get(d.get("nivel_matematica", "iniciante"), 0),
        map_atencao.get(d.get("atencao", "baixa"), 0),
        1 if d.get("interesse_imagem") else 0,
        1 if d.get("interesse_numeros") else 0,
        1 if d.get("interesse_jogos") else 0,
    ]
