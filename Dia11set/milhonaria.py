import numpy as np
import matplotlib.pyplot as plt
import math

# --- Probabilidade Teórica ---
# Combinações possíveis
total_combinacoes = math.comb(50, 6) * math.comb(6, 2)
p_teorica = 1 / total_combinacoes

# --- Simulação ---
n_simulacoes = 1_000_000  # pode aumentar, mas demora bastante
acertos = 0

# Aposta fixa do jogador
aposta_numeros = set(np.random.choice(range(1, 51), size=6, replace=False))
aposta_extras = set(np.random.choice(range(1, 7), size=2, replace=False))

for _ in range(n_simulacoes):
    # Sorteio dos 6 números principais
    sorteio_numeros = set(np.random.choice(range(1, 51), size=6, replace=False))
    # Sorteio dos 2 extras
    sorteio_extras = set(np.random.choice(range(1, 7), size=2, replace=False))

    # Comparação exata (6 + 2)
    if (sorteio_numeros == aposta_numeros) and (sorteio_extras == aposta_extras):
        acertos += 1

p_empirica = acertos / n_simulacoes

# --- Exibição ---
print(f"Probabilidade teórica: {p_teorica:.10f}")
print(f"Probabilidade empírica: {p_empirica:.10f}")
print(f"Acertos em {n_simulacoes:,} simulações: {acertos}")

# --- Gráfico ---
plt.bar(["Teórica"], [p_teorica], color="red", label="Teórica")
plt.bar(["Empírica"], [p_empirica], color="blue", label="Empírica")
plt.yscale("log")
plt.ylabel("Probabilidade (escala log)")
plt.title("Probabilidade de acertar a aposta (6/50 + 2/6)")
plt.legend()
plt.show()
