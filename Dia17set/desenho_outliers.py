import numpy as np
import matplotlib.pyplot as plt

dados = [10, 12, 12, 15, 18, 20, 22, 100]

# Cálculo dos outliers
media = np.mean(dados)
desvio = np.std(dados)
outliers = [x for x in dados if abs(x - media) > 2*desvio]

# Impressão
print("Outliers:", outliers)

# Plot do boxplot
plt.boxplot(dados, vert=False)
plt.title('Boxplot dos Dados com Outlier')
plt.xlabel('Valores')
plt.grid(True)
plt.show()