import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def estatisticas_descritivas(csv_path):
    # Carregar dataset
    df = pd.read_csv(csv_path)
    print(f"\n📂 Dataset carregado com {df.shape[0]} linhas e {df.shape[1]} colunas.\n")
    
    # Selecionar apenas colunas numéricas
    num_cols = df.select_dtypes(include=np.number).columns
    
    if len(num_cols) == 0:
        print("⚠️ O dataset não possui colunas numéricas para análise.")
        return
    
    resultados = {}
    
    for col in num_cols:
        dados = df[col].dropna()  # remover NaN
        
        estatisticas = {
            "média": np.mean(dados),
            "mediana": np.median(dados),
            "moda": stats.mode(dados, keepdims=True).mode[0],
            "variância": np.var(dados, ddof=1),  # ddof=1 para variância amostral
            "desvio padrão": np.std(dados, ddof=1),
            "assimetria": stats.skew(dados),
            "curtose": stats.kurtosis(dados)
        }
        resultados[col] = estatisticas
        
        print(f"\n📊 Estatísticas para '{col}':")
        for k, v in estatisticas.items():
            print(f"   {k:15}: {v:.4f}")
        
        # Histogramas
        plt.figure(figsize=(10,4))
        plt.subplot(1,2,1)
        sns.histplot(dados, kde=True, bins=20, color="skyblue")
        plt.title(f"Histograma - {col}")
        
        # Boxplot
        plt.subplot(1,2,2)
        sns.boxplot(x=dados, color="lightgreen")
        plt.title(f"Boxplot - {col}")
        
        plt.tight_layout()
        plt.show()
    
    return pd.DataFrame(resultados).T


# ----------------- EXEMPLO DE USO -----------------
estatisticas = estatisticas_descritivas("dataset_exemplo.csv")
print(estatisticas)