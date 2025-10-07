import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

# 1. Criar um dataset simples (ou usar um CSV real)
data = {
    'mensagem': [
        'Ganhe dinheiro rápido com este truque!',
        'Oi amigo, vamos sair hoje?',
        'Oferta exclusiva para você, clique agora',
        'Promoção imperdível, compre já',
        'Nos vemos amanhã no trabalho',
        'Você ganhou um prêmio, envie seus dados',
        'Reunião confirmada para segunda-feira'
    ],
    'spam': [1, 0, 1, 1, 0, 1, 0]  # 1 = spam, 0 = não spam
}

df = pd.DataFrame(data)

# 2. Pré-processamento
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['mensagem'])
y = df['spam']

# 3. Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. Treinar modelo
model = MultinomialNB()
model.fit(X_train, y_train)

# 5. Testar modelo
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# 6. Entrada do usuário
entrada = input("Digite uma mensagem: ")
entrada_vectorizada = vectorizer.transform([entrada])
prob_spam = model.predict_proba(entrada_vectorizada)[0][1]

print(f"Probabilidade de SPAM: {prob_spam:.2f}")
print("Classificação:", "SPAM" if prob_spam > 0.5 else "NÃO SPAM")
