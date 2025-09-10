import numpy as np
import matplotlib.pyplot as plt

# Valores de x
x = np.linspace(0.1, 5, 400)  # Começa em 0.1 para evitar log(0)

# Funções
y_linear = x
y_polinomial = x**3 - 3*x**2 + 2*x  # exemplo de polinômio cúbico
y_logaritmica = np.log(x)
y_exponencial = np.exp(x/2)  # dividir por 2 para não explodir muito rápido

# Criar gráfico
plt.figure(figsize=(10,6))

plt.plot(x, y_linear, label='Linear: y = x', color='blue', linewidth=2)
plt.plot(x, y_polinomial, label='Polinomial: y = x³ - 3x² + 2x', color='green', linewidth=2)
plt.plot(x, y_logaritmica, label='Logarítmica: y = log(x)', color='orange', linewidth=2)
plt.plot(x, y_exponencial, label='Exponencial: y = e^(x/2)', color='red', linewidth=2)

# Personalização
plt.title('Comparação de Funções', fontsize=16)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True)
plt.ylim(-5, 15)  # Ajustar para melhor visualização
plt.show()
