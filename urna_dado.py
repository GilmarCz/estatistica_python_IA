# Imports principais (execute primeiro)
import random                # Biblioteca para geração de números aleatórios
import math                  # Biblioteca com funções matemáticas (não foi usada neste trecho)
from collections import Counter  # Estrutura útil para contagem de elementos (não foi usada aqui)
import numpy as np           # Biblioteca para cálculos numéricos e manipulação de arrays
import matplotlib.pyplot as plt  # Biblioteca para visualização gráfica (não foi usada aqui)

# Bibliotecas de ciência de dados/IA
from sklearn.feature_extraction.text import CountVectorizer  # Transforma textos em vetores de contagem de palavras (não usado aqui)
from sklearn.naive_bayes import MultinomialNB, GaussianNB    # Classificadores Naive Bayes (não usados neste código)
from sklearn.model_selection import train_test_split         # Função para dividir dataset em treino/teste (não usado aqui)
from sklearn.datasets import make_classification             # Função para gerar datasets artificiais (não usado aqui)
from sklearn.metrics import roc_curve, auc                   # Métricas para avaliação de modelos (não usadas aqui)

# Bibliotecas científicas
from scipy import stats      # Estatística e distribuições (não usado neste trecho)
from scipy import integrate  # Funções de integração numérica (não usado neste trecho)

# Reprodutibilidade
random.seed(42)              # Define a semente do gerador de números aleatórios da biblioteca random
np.random.seed(42)           # Define a semente para a geração de números aleatórios do NumPy
# Assim, os resultados se repetem em diferentes execuções

# Solução (Exemplo 1 - Urna com bolas coloridas)
urna = ["vermelha"] * 3 + ["azul"] * 2   # Cria uma lista com 3 bolas vermelhas e 2 azuis

# 1) Teórica
p_teorica = 3 / 5   # Probabilidade teórica de tirar uma bola vermelha (3 vermelhas em 5 bolas)

# 2) Simulação (probabilidade experimental)
n = 10_000                                      # Número de sorteios simulados  | o 10_000 = 10000
sorteios = [random.choice(urna) for _ in range(n)]  # Escolhe aleatoriamente uma bola da urna n vezes
p_exp = sorteios.count("vermelha") / n          # Calcula a frequência relativa de bolas vermelhas

# Exibe os resultados
print(f"Probabilidade teórica (vermelha): {p_teorica:.4f}")      
# :.4f -> formata com 4 casas decimais
print(f"Probabilidade experimental (vermelha): {p_exp:.4f}")
print(f"Erro absoluto: {abs(p_teorica - p_exp):.4f}")
# Erro absoluto = diferença entre a probabilidade teórica e experimental

# Solução (Exemplo 2 - Dado de 6 lados)
lados = [1,2,3,4,5,6]          # Valores possíveis em uma rolagem de dado
p_teorica = 3 / 6              # Probabilidade teórica de sair um número par (2,4,6)

N = 100_000                    # Número de rolagens simuladas | | o 100_000 = 100000
rolagens = np.random.choice(lados, size=N, replace=True)  
# Simula N lançamentos de um dado, com reposição (replace=True)

p_exp = np.isin(rolagens, [2,4,6]).mean()  
# Verifica se cada rolagem é par e calcula a média (freq. relativa)

# Exibe os resultados
print(f"Probabilidade teórica (par): {p_teorica:.4f}")
print(f"Probabilidade experimental (par): {p_exp:.4f}")
print(f"Erro absoluto: {abs(p_teorica - p_exp):.4f}")
