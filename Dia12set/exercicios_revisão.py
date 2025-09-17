# Média, Mediana e Moda
# Calcule medidas de tendência central
# Crie uma lista de 10 números aleatórios entre 1 e 50
# Calcule a média, mediana e moda
# Use numpy e statistics

import numpy as np
import statistics as stats
import random

# Criar lista de 10 números aleatórios entre 1 e 50
numeros = [random.randint(1, 50) for _ in range(10)]

# Calcular medidas de tendência central
#media = np.mean(numeros)
#mediana = np.median(numeros)
media = stats.mean(numeros)
mediana = stats.median(numeros)
moda = stats.multimode(numeros)  # suporta múltiplas modas

# Exibir resultados
print("Lista de números:", numeros)
print(f"Média: {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}\n")

# Variância e Desvio Padrão
# Meça a dispersão dos dados.
# Utilize a lista numeros1
# Calcule a variância e o desvio padrão

numeros1 = [12,15,12,18,20,15,22,19,15,10]

# Variância
variancia_numpy = np.var(numeros1)       # população
variancia_stats = stats.pvariance(numeros1)      # população

# Desvio padrão
desvio_numpy = np.std(numeros1)          # população
desvio_stats = stats.pstdev(numeros1)            # população
media1 = stats.mean(numeros1)
mediana1 = stats.median(numeros1)
moda1 = stats.multimode(numeros1)

print("Lista:", numeros1)
print(f"Variância (numpy): {variancia_numpy:.2f}")
print(f"Variância (statistics): {variancia_stats:.2f}")
print(f"Desvio padrão (numpy): {desvio_numpy:.2f}")
print(f"Desvio padrão (statistics): {desvio_stats:.2f}")
print(f"Média: {media1:.2f}")
print(f"Mediana: {mediana1}")
print(f"Moda: {moda1}\n")

# Distribuição de Frequência
# Conte quantas vezes cada valor aparece
# Crie um histograma dos números da lista numeros1, usando o matplotlib
# Mostre a frequencia de cada número usando um dicionário

import matplotlib.pyplot as plt
from collections import Counter

# Frequência com Counter (gera um dicionário)
frequencia = Counter(numeros1)
freq = {x:numeros1.count(x) for x in set (numeros1)}

print("Frequência de cada número:", (frequencia))
print("Frequência de cada número:", (freq))

# Histograma
plt.hist(numeros1, bins=range(min(numeros1), max(numeros1) + 2), edgecolor='black', alpha=0.7)
plt.title("Histograma da Lista")
plt.xlabel("Números")
plt.ylabel("Frequência")
plt.show()
