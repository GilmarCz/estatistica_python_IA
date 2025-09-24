import numpy as np
import matplotlib.pyplot as plt
dados_normais = np.random.normal(loc=50, scale=10, size=100)
plt.hist(dados_normais, bins=10, edgecolor='black')
plt.title('Histograma de Dados Aleatórios Normais')
plt.show()
