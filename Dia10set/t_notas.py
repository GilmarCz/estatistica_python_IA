import numpy as np
from scipy import stats

# --- Parte 1 ---
notas_iniciais = [72, 68, 71, 69, 73, 74, 70, 67, 72, 71]

media_inicial = np.mean(notas_iniciais)
desvio_inicial = np.std(notas_iniciais, ddof=1)  # ddof=1 para amostral
print("Média inicial:", media_inicial)
print("Desvio padrão inicial:", desvio_inicial)

# Teste t (H0: média = 70)
t_stat, p_valor = stats.ttest_1samp(notas_iniciais, popmean=70)
print("t =", t_stat, "p =", p_valor)

# --- Parte 2 ---
notas_novas = [75, 78, 77, 74, 76, 79, 80, 81, 77, 76, 78, 75]

media_nova = np.mean(notas_novas)
desvio_novo = np.std(notas_novas, ddof=1)
print("\nMédia nova:", media_nova)
print("Desvio padrão novo:", desvio_novo)

# Teste t (H0: média = 70)
t_stat2, p_valor2 = stats.ttest_1samp(notas_novas, popmean=70)
print("t =", t_stat2, "p =", p_valor2)