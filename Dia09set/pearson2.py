import numpy as np
x = np.array([-1, 0, 1])
y = np.array([1, 0, -1])  # y = -x (correlação -1)

corr = np.corrcoef(x, y)[0, 1]
print("1a.Correlação de Pearson:", corr)
x = np.array([-1, 0, 1])
y = np.array([1, 0, 1])  # y não é linearmente relacionada com x

corr = np.corrcoef(x, y)[0, 1]
print("2a.Correlação de Pearson:", corr)

