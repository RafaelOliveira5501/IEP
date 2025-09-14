# backend/routers/alunos.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db
from ..models_sql import Aluno
from ..schemas import AlunoCreate

router = APIRouter()

@router.post("/aluno", status_code=201)
def create_aluno(payload: AlunoCreate, db: Session = Depends(get_db)):
    novo = Aluno(
        nome = payload.nome,
        idade = payload.idade,
        nivel_leitura = payload.nivel_leitura,
        nivel_matematica = payload.nivel_matematica,
        atencao = payload.atencao,
        interesse_imagem = payload.interesse_imagem,
        interesse_numeros = payload.interesse_numeros,
        interesse_jogos = payload.interesse_jogos,
    )
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return {"id": novo.id}
