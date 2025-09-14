# backend/ml/train_model.py
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from .preprocess import encode_features

# Carregar CSV com dados preparados (data/processed/alunos_clean.csv)
df = pd.read_csv("data/processed/alunos_clean.csv")

# Defina colunas de features e labels conforme combinamos
feature_cols = ["idade", "nivel_leitura", "nivel_matematica", "atencao",
                "interesse_imagem", "interesse_numeros", "interesse_jogos"]

# Labels (exemplos) - adapte para seu conjunto reduzido de insights
label_cols = [
    "metodo_atividades_curtas",
    "metodo_usar_imagens",
    "metodo_jogos_educativos",
    "desafio_leitura",
    "desafio_atencao"
]

# Preparar X com codificação simples
def encode_row(row):
    d = {
        "idade": row["idade"],
        "nivel_leitura": row["nivel_leitura"],
        "nivel_matematica": row["nivel_matematica"],
        "atencao": row["atencao"],
        "interesse_imagem": row["interesse_imagem"],
        "interesse_numeros": row["interesse_numeros"],
        "interesse_jogos": row["interesse_jogos"],
    }
    return encode_features(d)

X = df[feature_cols].apply(lambda r: encode_features(r), axis=1).tolist()
X = pd.DataFrame(X, columns=feature_cols)

y = df[label_cols]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelo multilabel com RandomForest
base = RandomForestClassifier(n_estimators=100, random_state=42)
clf = MultiOutputClassifier(base)
clf.fit(X_train, y_train)

# Avaliação rápida
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred, zero_division=0))

# Salvar modelo
joblib.dump(clf, "backend/ml/model.joblib")
print("Modelo salvo em backend/ml/model.joblib")
