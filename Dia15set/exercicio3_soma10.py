import numpy as np

# Número de simulações
n_sim = 10000

# Sorteio de três dados
dado1 = np.random.randint(1, 7, size=n_sim)
dado2 = np.random.randint(1, 7, size=n_sim)
dado3 = np.random.randint(1, 7, size=n_sim)

# Soma dos três dados
somas = dado1 + dado2 + dado3

# Evento: soma >= 10
P_soma_maior_igual_10 = np.mean(somas >= 10)

print(f"Probabilidade estimada (soma >= 10): {P_soma_maior_igual_10:.4f}")
