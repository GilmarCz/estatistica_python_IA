import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Ler o CSV com dados não lineares
dados = pd.read_csv('casas_quadraticas.csv')
X = dados[['Area']]
y = dados['Preco']

# ---------------------
# Regressão Linear
# ---------------------
modelo_linear = LinearRegression()
modelo_linear.fit(X, y)
y_linear = modelo_linear.predict(X)

# ---------------------
# Regressão Polinomial (grau 2)
# ---------------------
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
modelo_poly = LinearRegression()
modelo_poly.fit(X_poly, y)
y_poly = modelo_poly.predict(X_poly)

# ---------------------
# Plotando os gráficos
# ---------------------
plt.scatter(X, y, color='blue', label='Dados reais')
plt.plot(X, y_linear, color='red', label='Linear')
plt.plot(X, y_poly, color='green', linestyle='--', label='Polinomial grau 2')
plt.xlabel('Área (m²)')
plt.ylabel('Preço (R$)')
plt.title('Comparação: Linear x Polinomial (dados não lineares)')
plt.legend()
plt.show()

# ---------------------
# Coeficientes
# ---------------------
print("Coeficientes:")
print(f"Linear: coef={modelo_linear.coef_[0]:.2f}, intercepto={modelo_linear.intercept_:.2f}")
print(f"Polinomial grau 2: coef={modelo_poly.coef_}, intercepto={modelo_poly.intercept_:.2f}")