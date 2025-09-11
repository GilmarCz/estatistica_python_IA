import random
from collections import Counter
import matplotlib.pyplot as plt

# Espaço amostral de 3 dados (6x6x6 = 216 possíveis resultados)
# Aqui não listamos todos, pois vamos focar só no evento (6,6,6)

# Número de experimentos
N = 100000  # quanto maior, mais próximo da probabilidade teórica

# Simulação: gera N trios de lançamentos
resultados = [
    (random.choice([1,2,3,4,5,6]),
     random.choice([1,2,3,4,5,6]),
     random.choice([1,2,3,4,5,6]))
    for _ in range(N)
]

# Conta quantas vezes saiu (6,6,6)
contagem = Counter(resultados)
ocorrencias = contagem[(6,6,6)]

# Probabilidade experimental (empírica)
p_empirica = ocorrencias / N

# Probabilidade teórica
p_teorica = (1/6) ** 3

# --- Resultados ---
print(f"Probabilidade teórica (três 6): {p_teorica:.6f}")
print(f"Probabilidade empírica (simulação): {p_empirica:.6f}")
print(f"Ocorrências em {N} simulações: {ocorrencias}")

# --- Gráfico ---
plt.bar(["Teórica", "Empírica"], [p_teorica, p_empirica], width=0.4, color=["red", "blue"])
plt.ylabel("Probabilidade")
plt.title("Probabilidade de sair (6,6,6) em três dados")
plt.grid(axis="y", alpha=0.3)
plt.show()
