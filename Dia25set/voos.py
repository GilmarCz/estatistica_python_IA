import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Carregamento dos dados
df = pd.read_csv('dados1.csv')

# Renomeando colunas para facilitar a manipulação
df = df.rename(columns={
    'Distância (km)': 'Distancia_km',
    'Ocupação (%)': 'Ocupacao',
    'Receita (R$)': 'Receita_R'
})

# Exploração inicial dos dados
print(df.info())
print(df.head())
print("Valores nulos por coluna:\n", df.isnull().sum())

# Estatísticas descritivas
for col in ['Passageiros', 'Distancia_km', 'Ocupacao', 'Receita_R']:
    print(f"\nColuna: {col}")
    print("Média:", df[col].mean())
    print("Mediana:", df[col].median())
    print("Desvio padrão:", df[col].std())
    print("Variância:", df[col].var())

# Percentis de Receita
percentis = np.percentile(df['Receita_R'], [25, 50, 75])
print("Percentis Receita (R$):", percentis)

# Companhias com maior número de passageiros e maior receita
print("Companhia com maior receita total:", df.groupby('Companhia')['Receita_R'].sum().idxmax())
print("Companhia com maior número de passageiros:", df.groupby('Companhia')['Passageiros'].sum().idxmax())
print("Contagem de voos por companhia:\n", df['Companhia'].value_counts())
print("Receita média por companhia:\n", df.groupby('Companhia')['Receita_R'].mean())
print("Receita média por origem:\n", df.groupby('Aeroporto Origem')['Receita_R'].mean())
print("Aeroportos que concentram mais voos:\n", df['Aeroporto Origem'].value_counts().head(5))

# Gráficos opcionais
sns.histplot(df['Passageiros'], kde=True)
plt.title("Histograma de Passageiros")
plt.show()

sns.boxplot(data=df, x='Companhia', y='Receita_R')
plt.title("Boxplot da Receita por Companhia")
plt.show()

df['Distancia_km'].plot(kind='hist', bins=20)
plt.title("Histograma de Distância")
plt.xlabel("Distância (km)")
plt.show()

df[['Passageiros', 'Distancia_km', 'Ocupacao', 'Receita_R']].plot(kind='box', subplots=True, layout=(2,2))
plt.suptitle("Boxplots das Variáveis Numéricas")
plt.show()

sns.scatterplot(data=df, x='Distancia_km', y='Receita_R', hue='Companhia')
plt.title("Receita vs Distância por Companhia")
plt.show()

sns.heatmap(df[['Passageiros', 'Distancia_km', 'Ocupacao', 'Receita_R']].corr(), annot=True, cmap='Blues')
plt.title("Mapa de Calor das Correlações")
plt.show()
