from scipy import stats
import numpy as np

grupo_A = np.random.normal(70, 10, 30)
grupo_B = np.random.normal(65, 10, 30)

t_stat, p_val = stats.ttest_ind(grupo_A, grupo_B)
print("t =", t_stat, "p-valor =", p_val)