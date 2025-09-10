import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Exemplo de dados fictícios
# Altura em metros, Peso em kg
dados = pd.DataFrame({
    "altura": [1.60, 1.70, 1.80, 1.90, 1.65, 1.75],
    "peso":   [55, 65, 80, 95, 60, 78]
})

# Cálculo do IMC real
dados["IMC_real"] = dados["peso"] / (dados["altura"]**2)

# --------------------------
# 1) Regressão linear simples com altura e peso
# --------------------------
X1 = dados[["peso", "altura"]]  # variáveis explicativas
y = dados["IMC_real"]

modelo1 = LinearRegression()
modelo1.fit(X1, y)

dados["IMC_pred_simples"] = modelo1.predict(X1)

# --------------------------
# 2) Regressão linear com transformação (peso / altura²)
# --------------------------
X2 = (dados["peso"] / (dados["altura"]**2)).values.reshape(-1, 1)

modelo2 = LinearRegression()
modelo2.fit(X2, y)

dados["IMC_pred_transformado"] = modelo2.predict(X2)

# Mostrar resultados
print(dados)
print("\nCoeficientes modelo simples:", modelo1.coef_, "Intercepto:", modelo1.intercept_)
print("Coeficiente modelo transformado:", modelo2.coef_, "Intercepto:", modelo2.intercept_)