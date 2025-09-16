import random
from collections import Counter

espaco_amostral = [(a,b) for a in ['C','K'] for b in ['C','K']]
print("Espaço amostral:", espaco_amostral)

# Simulação
resultados = [(random.choice(['C','K']), random.choice(['C','K'])) for _ in range(10000)]
# print (resultados)
frequencias = Counter(resultados)
print(frequencias)