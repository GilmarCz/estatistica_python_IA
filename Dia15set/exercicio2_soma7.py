import numpy as np

# Número de simulações
n_sim = 10000

# Sorteio dos dois dados
dado1 = np.random.randint(1, 7, size=n_sim)  # valores de 1 a 6
dado2 = np.random.randint(1, 7, size=n_sim)

# Soma dos dois dados
somas = dado1 + dado2

# Evento 1: soma == 7
P_soma_7 = np.mean(somas == 7)

# Evento 2: soma >= 7
P_soma_maior_igual_7 = np.mean(somas >= 7)

print(f"Probabilidade estimada (soma = 7): {P_soma_7:.4f}")
print(f"Probabilidade estimada (soma >= 7): {P_soma_maior_igual_7:.4f}")
