# Imports principais (execute primeiro)
import random
import math
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

# Bibliotecas de ciência de dados/IA
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.metrics import roc_curve, auc

# Bibliotecas científicas
from scipy import stats
from scipy import integrate

# Reprodutibilidade
random.seed(42)
np.random.seed(42)
# Solução
urna = ["vermelha"] * 3 + ["azul"] * 2

# 1) Teórica
p_teorica = 3 / 5

# 2) Simulação
n = 10_000
sorteios = [random.choice(urna) for _ in range(n)]
p_exp = sorteios.count("vermelha") / n

print(f"Probabilidade teórica (vermelha): {p_teorica:.4f}")
print(f"Probabilidade experimental (vermelha): {p_exp:.4f}")
print(f"Erro absoluto: {abs(p_teorica - p_exp):.4f}")

# Solução
lados = [1,2,3,4,5,6]
p_teorica = 3 / 6  # {2,4,6}

N = 100_000
rolagens = np.random.choice(lados, size=N, replace=True)
p_exp = np.isin(rolagens, [2,4,6]).mean()

print(f"Probabilidade teórica (par): {p_teorica:.4f}")
print(f"Probabilidade experimental (par): {p_exp:.4f}")
print(f"Erro absoluto: {abs(p_teorica - p_exp):.4f}")