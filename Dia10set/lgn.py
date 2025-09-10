import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# Simulando lançamentos de moeda (1 = cara, 0 = coroa)
n_experimentos = 10000
lancamentos = np.random.choice([0, 1], size=n_experimentos, p=[0.5, 0.5])

# Média acumulada
medias_acumuladas = np.cumsum(lancamentos) / np.arange(1, n_experimentos + 1)

plt.plot(medias_acumuladas, label="Média acumulada")
plt.axhline(0.5, color="red", linestyle="--", label="Probabilidade real (0.5)")
plt.xlabel("Número de lançamentos")
plt.ylabel("Proporção de caras")
plt.legend()
plt.show()