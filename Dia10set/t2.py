from scipy import stats
import numpy as np
antes = np.random.normal(70, 5, 20)
depois = antes - np.random.normal(2, 2, 20)  # melhoraram em média 2 pontos

t_stat, p_val = stats.ttest_rel(antes, depois)
print("\nt =", t_stat, "p-valor =", p_val)
diferencas = antes - depois
print("Média da variação de peso:", np.mean(diferencas),"\n")
