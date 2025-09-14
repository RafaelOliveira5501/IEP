# backend/main.py
from fastapi import FastAPI
from .db import engine, Base
from .routers import insights, alunos
from .models_sql import Aluno, Insight

app = FastAPI(title="PEI Insights API (MVP)")

# criar tables (MVP). Em produção, use Alembic
Base.metadata.create_all(bind=engine)

app.include_router(insights.router, prefix="/insights", tags=["insights"])
app.include_router(alunos.router, prefix="", tags=["alunos"])

@app.get("/")
def root():
    return {"ok": True, "message": "API PEI rodando"}
