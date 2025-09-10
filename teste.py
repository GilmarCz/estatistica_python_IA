import numpy as np

# Definição dos naipes em Unicode
naipes_vermelhos = {"♥", "♦"}
naipes_pretos = {"♣", "♠"}
ranks = ['A'] + [str(i) for i in range(2,11)] + ['J','Q','K']
naipes = list(naipes_vermelhos | naipes_pretos)
baralho = [(r, n) for r in ranks for n in naipes]

# Cálculo teórico
p_teorica = 6 / 12

# Simulação
N = 200_000
amostras = np.random.choice(len(baralho), size=N, replace=True)

# Converter para arrays NumPy para operações vetoriais eficientes
ranks_amostra = np.array([baralho[i][0] for i in amostras])
naipes_amostra = np.array([baralho[i][1] for i in amostras])

figura = np.isin(ranks_amostra, ['J','Q','K'])
vermelha = np.isin(naipes_amostra, list(naipes_vermelhos))

fig_e_verm = np.mean(figura & vermelha)
p_fig = np.mean(figura)
p_exp = fig_e_verm / p_fig

print(f"P(vermelha | figura) teórica: {p_teorica:.4f}")
print(f"P(vermelha | figura) experimental: {p_exp:.4f}")
print(f"Erro absoluto: {abs(p_teorica - p_exp):.4f}\n")


import random
import math
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

# Configurar sementes para reprodutibilidade
random.seed(42)
np.random.seed(42)

# Definições
baralho_figuras = ['J', 'Q', 'K']
naipes = ['C', 'O', 'E', 'P']  # Copas, Ouros (vermelhas), Espadas, Paus (pretas)
cores = {'C': 'vermelha', 'O': 'vermelha', 'E': 'preta', 'P': 'preta'}

# Construção do baralho
numeros = list(range(2, 11)) + baralho_figuras
baralho = [(str(n), naipe) for n in numeros for naipe in naipes]

# Simulação da probabilidade condicional
def simular_prob_condicional(n_sim=100000):
    figuras_tiradas = 0
    vermelhas_figura_tiradas = 0
    
    for _ in range(n_sim):
        carta = random.choice(baralho)
        if carta[0] in baralho_figuras:
            figuras_tiradas += 1
            if cores[carta[1]] == 'vermelha':
                vermelhas_figura_tiradas += 1
                
    return vermelhas_figura_tiradas / figuras_tiradas if figuras_tiradas > 0 else 0

# Rodar simulação e obter resultado
prob_simulada = simular_prob_condicional()

print(f'Probabilidade condicional estimada pela simulação: {prob_simulada:.4f}')

# Visualização gráfica da convergência da simulação
def convergencia_simulacao(max_sim=100000, step=1000):
    resultados = []
    figuras_tiradas = 0
    vermelhas_figura_tiradas = 0

    for i in range(1, max_sim + 1):
        carta = random.choice(baralho)
        if carta[0] in baralho_figuras:
            figuras_tiradas += 1
            if cores[carta[1]] == 'vermelha':
                vermelhas_figura_tiradas += 1
        
        if i % step == 0 and figuras_tiradas > 0:
            resultados.append(vermelhas_figura_tiradas / figuras_tiradas)
    
    return resultados

resultados = convergencia_simulacao()

# Plot da convergência
plt.figure(figsize=(10, 6))
plt.plot(range(1000, 100001, 1000), resultados, label='Estimativa Simulada')
plt.axhline(y=0.5, color='r', linestyle='--', label='Valor Teórico (0.5)')
plt.xlabel('Número de Simulações')
plt.ylabel('Probabilidade Condicional Estimada')
plt.title('Convergência da Simulação da Probabilidade Condicional')
plt.legend()
plt.grid(True)
plt.show()
