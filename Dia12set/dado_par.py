import random
pares = [x for x in range(1,7) if x % 2 == 0]
prob_teorica = len(pares)/6

simulacoes = [random.randint(1,6) for _ in range(10000)]
freq_par = sum(1 for x in simulacoes if x % 2 == 0) / len(simulacoes)

print(f"Probabilidade: Teórica: {prob_teorica}, Simulada: {freq_par}")
