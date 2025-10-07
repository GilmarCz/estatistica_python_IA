import numpy as np
import matplotlib.pyplot as plt

# Definição da função
def f(x):
    return 2*x - 4

# Raiz
raiz = 4/2

# Intervalo de valores
x = np.linspace(-2, 5, 100)
y = f(x)
print ("Valores de x:", x[:10])
print ("Valores de y:",y[:10])
# Gráfico
plt.axhline(0, color="black", linewidth=1)
plt.axvline(0, color="black", linewidth=1)
plt.plot(x, y, label="f(x) = 2x - 4")
plt.scatter(raiz, 0, color="red", label=f"Raiz: x={raiz}")
plt.legend()
plt.grid(True)
plt.show()
