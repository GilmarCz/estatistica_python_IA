import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Ler o CSV com dados não lineares
dados = pd.read_csv('area_preco.csv')
X = dados[['Area']]
y = dados['Preco']

# Plotando os dados reais
plt.scatter(X, y, color='blue', label='Dados reais')

# Testar diferentes graus polinomiais
graus = [1, 2, 3, 4]
cores = ['red', 'green', 'orange', 'purple']

for grau, cor in zip(graus, cores):
    poly = PolynomialFeatures(degree=grau)
    X_poly = poly.fit_transform(X)
    modelo = LinearRegression()
    modelo.fit(X_poly, y)
    y_previsto = modelo.predict(X_poly)
    plt.plot(X, y_previsto, color=cor, linestyle='--' if grau > 1 else '-', label=f'Polinomial grau {grau}')

plt.xlabel('Área (m²)')
plt.ylabel('Preço (R$)')
plt.title('Comparação de Regressões Polinomiais')
plt.legend()
plt.show()