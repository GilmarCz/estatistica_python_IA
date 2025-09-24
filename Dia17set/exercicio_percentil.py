#Divida os dados em partes para análise.
# tarefa: Utilize a lista 
# numeros = [12, 15, 12, 18, 20, 15, 22, 19, 15, 10]
# Q1; Q2; Q3

import numpy as np 

numeros = [12, 15, 12, 18, 20, 15, 22, 19, 15, 10]

Q1 = np.percentile(numeros, 25)
Q2 = np.percentile(numeros, 50)
Q3 = np.percentile(numeros, 75)

print("👉 Percentil é um ponto que divide um conjunto de dados ordenados em 100 partes iguais.")
print(f"A lista: {numeros}\nSeu respectivos percentis:")
print(f"Q1: ", Q1," → calcula o percentil 25 (Q1), ou seja, o valor abaixo do qual estão 25% dos dados.") # → calcula o percentil 25 (Q1), ou seja, o valor abaixo do qual estão 25% dos dados.
print(f"Q2: ", Q2, " → calcula o percentil 50 (Q2), que é a mediana.") # → calcula o percentil 50 (Q2), que é a mediana.
print(f"Q3: ", Q3, " → calcula o percentil 75 (Q3), o valor abaixo do qual estão 75% dos dados.\n") # → calcula o percentil 75 (Q3), o valor abaixo do qual estão 75% dos dados.
print("⚡ Em outras palavras: percentil mostra em que posição relativa um valor está dentro do conjunto de dados.\n")