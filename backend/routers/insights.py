# backend/routers/insights.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import joblib
from ..db import get_db
from ..models_sql import Aluno, Insight
from ..schemas import InsightOut
from ..ml.preprocess import encode_features
from ..utils.rules import apply_rules
import os

router = APIRouter()
MODEL_PATH = os.getenv("MODEL_PATH", "backend/ml/model.joblib")
MODEL = None

def load_model():
    global MODEL
    if MODEL is None:
        MODEL = joblib.load(MODEL_PATH)
    return MODEL

@router.post("/generate/{aluno_id}", response_model=InsightOut)
def generate_insights(aluno_id: int, db: Session = Depends(get_db)):
    aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")

    features_dict = {
        "idade": aluno.idade,
        "nivel_leitura": aluno.nivel_leitura,
        "nivel_matematica": aluno.nivel_matematica,
        "atencao": aluno.atencao,
        "interesse_imagem": aluno.interesse_imagem,
        "interesse_numeros": aluno.interesse_numeros,
        "interesse_jogos": aluno.interesse_jogos,
    }

    model = load_model()
    x = encode_features(features_dict)
    y_pred = model.predict([x])[0]  # retorna array binário por label

    # Mapeamento das labels (mesmo usado no treino)
    label_names = [
        "metodo_atividades_curtas",
        "metodo_usar_imagens",
        "metodo_jogos_educativos",
        "desafio_leitura",
        "desafio_atencao"
    ]

    current_insights = {"forcas": [], "desafios": [], "metodos_recomendados": []}
    # Preencher a partir das previsões
    if y_pred[0]:
        current_insights["metodos_recomendados"].append("atividades curtas")
    if y_pred[1]:
        current_insights["metodos_recomendados"].append("usar imagens")
    if y_pred[2]:
        current_insights["metodos_recomendados"].append("jogos educativos")
    if y_pred[3]:
        current_insights["desafios"].append("dificuldade em leitura")
    if y_pred[4]:
        current_insights["desafios"].append("atenção limitada")

    # Aplicar regras para complementar/ajustar
    final = apply_rules(features_dict, current_insights)

    # Salvar no banco
    novo = Insight(aluno_id=aluno.id, insights=final)
    db.add(novo)
    db.commit()
    db.refresh(novo)

    return final
