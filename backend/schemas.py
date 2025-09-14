# backend/schemas.py
from pydantic import BaseModel
from typing import List, Optional

class AlunoCreate(BaseModel):
    nome: Optional[str]
    idade: int
    nivel_leitura: str
    nivel_matematica: str
    atencao: str
    interesse_imagem: bool = False
    interesse_numeros: bool = False
    interesse_jogos: bool = False

class InsightOut(BaseModel):
    forcas: List[str]
    desafios: List[str]
    metodos_recomendados: List[str]
