import numpy as np

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

corr = np.corrcoef(x, y)[0, 1]
print("Correlação de Pearson:", corr)