# Importar bibliotecas
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Ler o CSV
dados = pd.read_csv('casas.csv')

# Separar as variáveis
X = dados[['Area']]   # Variável independente
y = dados['Preco']    # Variável dependente

# Criar e treinar o modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Fazer previsões
y_previsto = modelo.predict(X)

# Mostrar coeficiente e intercepto
print(f"Coeficiente (preço por m²): {modelo.coef_[0]}")
print(f"Intercepto: {modelo.intercept_}")

# Comparar valores reais x previstos
resultado = pd.DataFrame({'Real': y, 'Previsto': y_previsto})
print(resultado)

# Plotar gráfico
plt.scatter(X, y, color='blue', label='Dados reais')
plt.plot(X, y_previsto, color='red', label='Linha de regressão')
plt.xlabel('Área (m²)')
plt.ylabel('Preço (R$)')
plt.title('Regressão Linear: Área x Preço')
plt.legend()
plt.show()