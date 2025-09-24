import numpy as np
altura = [160, 165, 170, 175, 180, 185, 160, 170, 175, 180]
peso = [55, 60, 65, 70, 75, 80, 58, 68, 72, 77]
correlacao = np.corrcoef(altura, peso)[0, 1]
print("Correlação de Pearson entre altura e peso:", correlacao)
