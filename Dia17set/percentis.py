import numpy as np
numeros = [12, 15, 12, 18, 20, 15, 22, 19, 15, 10]
percentis = np.percentile(numeros, [25, 50, 75])
print("Percentis 25, 50, 75:", percentis)
