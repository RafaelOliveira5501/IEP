# backend/models_sql.py
from sqlalchemy import Column, Integer, String, Boolean, JSON, DateTime, ForeignKey
from sqlalchemy.sql import func
from .db import Base

class Aluno(Base):
    __tablename__ = "alunos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=True)
    idade = Column(Integer, nullable=False)
    nivel_leitura = Column(String, nullable=False)
    nivel_matematica = Column(String, nullable=False)
    atencao = Column(String, nullable=False)
    interesse_imagem = Column(Boolean, default=False)
    interesse_numeros = Column(Boolean, default=False)
    interesse_jogos = Column(Boolean, default=False)

class Insight(Base):
    __tablename__ = "insights"
    id = Column(Integer, primary_key=True, index=True)
    aluno_id = Column(Integer, ForeignKey("alunos.id"), nullable=False)
    insights = Column(JSON, nullable=False)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
