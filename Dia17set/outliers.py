import numpy as np
dados = [10, 12, 12, 15, 18, 20, 22, 100]
media = np.mean(dados)
desvio = np.std(dados)
outliers = [x for x in dados if abs(x - media) > 2*desvio]
print("Outliers:", outliers)
