import random

# 1. Probabilidade teórica
pares = [x for x in range(1,7) if x % 2 == 0]
prob_teorica = len(pares) / 6

print("Probabilidade teórica de número par:", prob_teorica)

# 2. Simulação
n_lancamentos = 10000
lancamentos = [random.randint(1,6) for _ in range(n_lancamentos)]

# Contar pares
pares_obtidos = [x for x in lancamentos if x in pares]
prob_empirica = len(pares_obtidos) / n_lancamentos

print("Probabilidade teórica:", prob_teorica)
print("Probabilidade empírica:", prob_empirica)
print("Diferença:", abs(prob_teorica - prob_empirica))