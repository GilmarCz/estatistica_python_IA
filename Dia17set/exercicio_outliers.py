# Detecte valores fora da distribuição comum.
# Calcule o desvio padrão e identifique números que estão a mais de 2 desvios padrões da média

import numpy as np 

# Lista de números
numeros = [12, 15, 12, 18, 20, 15, 22, 19, 15, 10]

# Calcular média e desvio padrão
media = np.mean(numeros)
desvio = np.std(numeros)

# Limites para identificar outliers (± 2 desvios da média)
limite_inferior = media - 2 * desvio
limite_superior = media + 2 * desvio

# Identificar valores fora do intervalo
outliers = [x for x in numeros if x < limite_inferior or x > limite_superior]

# Exibir resultados
print(f"Média: {media:.2f}")
print(f"Desvio padrão: {desvio:.2f}")
print(f"Limite inferior: {limite_inferior:.2f}")
print(f"Limite superior: {limite_superior:.2f}")
print("Outliers encontrados:", outliers if outliers else "Nenhum")
