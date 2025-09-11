import numpy as np
import matplotlib.pyplot as plt
import math

# --- Probabilidades Teóricas ---
# Total de combinações possíveis
total_combinacoes = math.comb(60, 6)

# Probabilidades de cada acerto
p_sena = 1 / total_combinacoes
p_quina = math.comb(6, 5) * math.comb(60-6, 1) / total_combinacoes
p_quadra = math.comb(6, 4) * math.comb(60-6, 2) / total_combinacoes

print("Probabilidades Teóricas:")
print(f"Sena (6 acertos): {p_sena:.12f} (~1 em {1/p_sena:,.0f})")
print(f"Quina (5 acertos): {p_quina:.9f} (~1 em {1/p_quina:,.0f})")
print(f"Quadra (4 acertos): {p_quadra:.7f} (~1 em {1/p_quadra:,.0f})")

# --- Simulação ---
n_simulacoes = 1_000_000
resultados = {"Sena": 0, "Quina": 0, "Quadra": 0}

# Aposta fixa do jogador
aposta = set(np.random.choice(range(1, 61), size=6, replace=False))

for _ in range(n_simulacoes):
    sorteio = set(np.random.choice(range(1, 61), size=6, replace=False))
    acertos = len(aposta.intersection(sorteio))

    if acertos == 6:
        resultados["Sena"] += 1
    elif acertos == 5:
        resultados["Quina"] += 1
    elif acertos == 4:
        resultados["Quadra"] += 1

# Frequências empíricas
p_empirica_sena = resultados["Sena"] / n_simulacoes
p_empirica_quina = resultados["Quina"] / n_simulacoes
p_empirica_quadra = resultados["Quadra"] / n_simulacoes

print("\nProbabilidades Empíricas (simulação):")
print(f"Sena: {p_empirica_sena:.12f}")
print(f"Quina: {p_empirica_quina:.9f}")
print(f"Quadra: {p_empirica_quadra:.7f}")
print(f"Acertos em {n_simulacoes:,} simulações → {resultados}")

# --- Gráfico ---
categorias = ["Sena", "Quina", "Quadra"]
teoricas = [p_sena, p_quina, p_quadra]
empiricas = [p_empirica_sena, p_empirica_quina, p_empirica_quadra]

x = np.arange(len(categorias))
largura = 0.35

plt.bar(x - largura/2, teoricas, largura, label="Teórica", color="red")
plt.bar(x + largura/2, empiricas, largura, label="Empírica", color="blue")
plt.xticks(x, categorias)
plt.yscale("log")
plt.ylabel("Probabilidade (escala log)")
plt.title("Mega-Sena: Probabilidade Teórica vs Empírica")
plt.legend()
plt.show()
