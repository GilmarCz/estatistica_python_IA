import pandas as pd
import numpy as np

# Criar dataset fictício
np.random.seed(42)
dados = {
    "idade": np.random.normal(30, 5, 100),          # média 30, desvio 5
    "peso": np.random.normal(70, 10, 100),          # média 70, desvio 10
    "altura": np.random.normal(1.70, 0.1, 100),     # média 1.70m, desvio 0.1
}

df = pd.DataFrame(dados)

# Salvar como CSV
df.to_csv("dataset_exemplo.csv", index=False)
print("✅ Arquivo dataset_exemplo.csv criado!")