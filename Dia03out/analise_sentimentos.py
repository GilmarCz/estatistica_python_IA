import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# 1. Carregar CSV
df = pd.read_csv("sentimentos.csv")

X = df['texto']
y = df['sentimento']

# 2. Vetorização
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# 3. Treinamento do modelo
model = LogisticRegression(max_iter=1000)
model.fit(X_vec, y)

# 4. Função para classificar uma frase
def classificar_sentimento(frase):
    frase_vec = vectorizer.transform([frase])  # <-- usar o mesmo vectorizer treinado
    probas = model.predict_proba(frase_vec)[0]
    classes = model.classes_
    
    print("Probabilidades:")
    for classe, p in zip(classes, probas):
        print(f"{classe}: {p*100:.2f}%")
    
    pred = model.predict(frase_vec)[0]
    print("\nClassificação final:", pred)

# 5. Teste com frase do usuário
frase_usuario = input("Digite uma frase para análise de sentimento: ")
classificar_sentimento(frase_usuario)
