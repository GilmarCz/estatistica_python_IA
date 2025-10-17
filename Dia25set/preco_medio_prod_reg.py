import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Carregar os dados ---
df = pd.read_csv("dados.csv")  # substitua pelo nome correto do seu CSV

# --- Agrupar ---
df_grouped = df.groupby(['Produto','Região'])['Preço Unitário'].mean().reset_index()
print (df_grouped)
# --- Pivot para facilitar ---
pivot = df_grouped.pivot(index='Produto', columns='Região', values='Preço Unitário')

# --- 1. Gráfico de barras agrupadas ---
pivot.plot(kind='bar', figsize=(10,6))
plt.title('Preço Médio por Produto e Região - Barras Agrupadas')
plt.ylabel('Preço Médio (R$)')
plt.xlabel('Produto')
plt.legend(title='Região')
plt.xticks(rotation=45)
plt.show()

# --- 2. Gráfico de linhas ---
pivot.plot(kind='line', marker='o', figsize=(10,6))
plt.title('Preço Médio por Produto e Região - Linha')
plt.ylabel('Preço Médio (R$)')
plt.xlabel('Produto')
plt.legend(title='Região')
plt.grid(True)
plt.show()

# --- 3. Gráfico de barras horizontais ---
plt.figure(figsize=(10,6))
sns.barplot(data=df_grouped, x='Preço Unitário', y='Produto', hue='Região')
plt.title('Preço Médio por Produto e Região - Barras Horizontais')
plt.xlabel('Preço Médio (R$)')
plt.ylabel('Produto')
plt.show()
