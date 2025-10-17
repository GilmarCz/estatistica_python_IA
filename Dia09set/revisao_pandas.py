import pandas as pd

# Criando um DataFrame
dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos'],
    'Idade': [23, 35, 31],
    'Cidade': ['SP', 'RJ', 'BH']
}

df = pd.DataFrame(dados)

# Exportando para CSV sem índice
df.to_csv('saida.csv', index=False)
print (df)
print ("\n")
print(df.head())     # Primeiras linhas
print ("\n")
print(df.tail())     # Últimas linhas
print ("\n")
print(df.info())     # Informações do DataFrame
print ("\n")
print(df.describe()) # Estatísticas descritivas
print ("\n")
print(df.shape)      # Linhas e colunas
