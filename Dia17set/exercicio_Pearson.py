#Correlação de person
import numpy as np  
# Vetor altura
altura = np.array([160,165,170,175,180,185,160,170,175,180])
# Vetor peso
peso   = np.array([55,60,65,70,75,80,58,68,72,77])
 
# Calcula a matriz de correlação de Pearson entre altura e peso
# np.corrcoef retorna uma matriz 2x2:
#   [ [1, correlação],
#     [correlação, 1] ]
# O valor de interesse é a posição [0,1] (ou [1,0]), que é a correlação entre altura e peso
corr = np.corrcoef(altura, peso)[0, 1]
 
# Exibe o resultado da correlação
print("1a.Correlação de Pearson:", corr)