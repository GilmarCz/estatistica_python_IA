import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Ler CSV
import pandas as pd

df = pd.read_csv('producao.csv', parse_dates=['Data'])
print(df)
df = pd.read_csv("producao.csv", parse_dates=['Data'])
# Agrupar por Data e Turno para somar as peças e defeituosas
grouped = df.groupby(['Data', 'Turno']).sum().reset_index()
print(grouped)

# Pivot para heatmap (Data x Turno, valor = Peças Produzidas)
pivot = grouped.pivot(index='Data', columns='Turno', values='Peças_Produzidas')

# Plot Heatmap
plt.figure(figsize=(8,5))
sns.heatmap(pivot, annot=True, fmt="d", cmap="YlGnBu")
plt.title("Heatmap: Produção de Peças por Turno")
plt.show()

# Gráfico de dispersão (Defeituosas x Peças Produzidas)
plt.figure(figsize=(8,5))
sns.scatterplot(data=grouped, x='Peças_Produzidas', y='Defeituosas', hue='Turno', s=100)
plt.title("Dispersão: Peças Produzidas x Defeituosas")
plt.xlabel("Peças Produzidas")
plt.ylabel("Peças Defeituosas")
plt.grid(True)
plt.show()