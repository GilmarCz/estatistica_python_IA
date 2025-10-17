import numpy as np
import pandas as pd
from scipy.stats import skew, kurtosis

# Definir a seed para reprodutibilidade
np.random.seed(42)

# Gerar dados normais centrados em 2, com baixa variância
dados_normais = np.random.normal(loc=2, scale=0.2, size=1000)

# Gerar outliers positivos com distribuição exponencial (assimetria positiva)
outliers = np.random.exponential(scale=10, size=20)

# Combinar os dados
dados_com_outliers = np.concatenate([dados_normais, outliers])

# Criar DataFrame
df = pd.DataFrame({
    'id': range(1, len(dados_com_outliers) + 1),
    'valor': dados_com_outliers
})

# Calcular skewness e kurtosis
skew_val = skew(dados_com_outliers)
kurt_val = kurtosis(dados_com_outliers)

print("Skewness:", skew_val)
print("Kurtosis:", kurt_val)

# Salvar o arquivo CSV
df.to_csv("dados_skew_kurtosis.csv", index=False)
print("Arquivo 'dados_skew_kurtosis.csv' criado com sucesso!")