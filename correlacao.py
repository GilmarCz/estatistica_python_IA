import numpy as np
from scipy.stats import pearsonr

x = np.random.rand(100)
y = 2 * x + np.random.normal(0, 0.1, 100)

correlacao, _ = pearsonr(x, y)
print("Correlação de Pearson:", correlacao)
