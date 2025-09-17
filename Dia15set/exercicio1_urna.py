import numpy as np

# Urna com 3 vermelhas (R) e 2 azuis (B)
bolas = ['R','R','R','B','B']
n_sim = 10000

# Sorteios com reposição
sorteios = np.random.choice(bolas, size=n_sim, replace=True)

# Evento A: bola azul
A = sorteios == 'B'

# Evento B: índice múltiplo de 5
B = np.arange(n_sim) % 5 == 0

# Probabilidade de (A OU B)
P_ou = np.mean(A | B)

# Probabilidade de (A E B)
P_e = np.mean(A & B)

print(f"Probabilidade (bola azul OU índice múltiplo de 5) ~ {P_ou:.4f}")
print(f"Probabilidade (bola azul E índice múltiplo de 5) ~ {P_e:.4f}")
