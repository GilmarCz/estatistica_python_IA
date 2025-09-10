# Você tem as notas de 12 alunos em uma prova de matemática:
# notas_alunos = [82, 76, 88, 91, 69, 73, 85, 79, 90, 77, 84, 80]
# O objetivo é verificar se a média dessas notas difere significativamente de 75 usando um teste t de uma amostra

import numpy as np
from scipy import stats

# --- Parte 1 ---
notas_alunos = [82, 76, 88, 91, 69, 73, 85, 79, 90, 77, 84, 80]

media_alunos = np.mean(notas_alunos)
desvio_alunos = np.std(notas_alunos, ddof=1)  # ddof=1 para amostral
print("Média inicial:", media_alunos)
print("Desvio padrão inicial:", desvio_alunos)

# Teste t (H0: média = 75)
t_stat, p_valor = stats.ttest_1samp(notas_alunos, popmean=75)
print("t =", t_stat, "p =", p_valor,"\n")