import numpy as np

bolas = np.array(['R', 'R', 'R', 'B', 'B'])
n_sim = 10000

# Sorteia 3 bolas com reposição em cada simulação
sorteios = np.random.choice(bolas, size=(n_sim, 3), replace=True)

# Evento: todas as 3 são 'R'
A = np.all(sorteios == 'R', axis=1)

P_sim = np.mean(A)
print(f"Probabilidade de 3 vermelhas em sequência (com reposição) ~ {P_sim:.4f}")
