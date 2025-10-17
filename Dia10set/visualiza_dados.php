import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Carrega o arquivo CSV gerado anteriormente
df = pd.read_csv('dados_skew_kurtosis.csv')

# Tamanho da figura
plt.figure(figsize=(14, 6))

# Histograma
plt.subplot(1, 2, 1)
sns.histplot(df['valor'], bins=50, kde=True, color='skyblue')
plt.title('Histograma com KDE (Distribuição dos Dados)')
plt.xlabel('Valor')
plt.ylabel('Frequência')

# Boxplot
plt.subplot(1, 2, 2)
sns.boxplot(x=df['valor'], color='lightgreen')
plt.title('Boxplot dos Dados')

# Mostrar os gráficos
plt.tight_layout()
plt.show()