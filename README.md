# IEP – Plataforma de Insights Educacionais

Projeto de Inteligência Artificial e Gestão Educacional para gerar **insights pedagógicos personalizados** para alunos com deficiência intelectual leve a moderada. O sistema combina FastAPI, PostgreSQL e Machine Learning para registrar alunos, analisar dados e sugerir recomendações educacionais.

---

## **Funcionalidades**

* Registro de alunos com dados acadêmicos e interesses.
* Armazenamento em banco de dados PostgreSQL.
* Geração automática de insights com modelo de Machine Learning (RandomForestClassifier).
* Interface web interativa via **Streamlit**.
* API RESTful para integração e testes.

---

## **Pré-requisitos**

* Python 3.11+
* PostgreSQL
* Git
* pip

Recomendado criar um ambiente virtual para evitar conflitos de dependências:

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

---

## **Instalação**

1. Clonar o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
cd IEP
```

2. Instalar dependências:

```bash
pip install -r requirements.txt
```

---

## **Configuração do Banco de Dados**

1. Criar banco e usuário:

```sql
CREATE DATABASE pei_db;
CREATE USER pei_user WITH PASSWORD 'pei_pass';
GRANT ALL PRIVILEGES ON DATABASE pei_db TO pei_user;
```

2. Criar tabelas principais (exemplo: `alunos`):

```sql
CREATE TABLE alunos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INTEGER NOT NULL,
    serie VARCHAR(50),
    necessidades_especiais TEXT,
    nivel_matematica VARCHAR(50),
    atencao VARCHAR(50),
    interesse_imagem BOOLEAN,
    interesse_numeros BOOLEAN,
    interesse_jogos BOOLEAN
);
```

3. Outras tabelas, como `insights`, devem ser criadas conforme o modelo do projeto.

---

## **Configuração do Projeto**

1. Criar arquivo `.env` com as variáveis de ambiente do banco:

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=pei_db
DB_USER=pei_user
DB_PASSWORD=1234
```

2. Treinar o modelo de Machine Learning (ou usar o modelo pré-treinado):

```bash
python backend/ml/train_model.py
```

---

## **Rodando o Projeto**

1. Backend (FastAPI):

```bash
uvicorn backend.main:app --reload
```

* URL padrão: `http://127.0.0.1:8000`
* Endpoints principais:

  * `POST /aluno` → registrar aluno e gerar insight
  * `GET /alunos` → listar alunos

2. Frontend (Streamlit):

```bash
streamlit run frontend/app.py
```

* URL padrão: `http://localhost:8501`

---

## **Testando**

1. Registrar um aluno via Streamlit ou via API (`POST /aluno`).
2. Conferir se os insights foram gerados corretamente.
3. Verificar se os dados estão no banco de dados.
