import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Leitura do CSV
df = pd.read_csv('dados1.csv')

# Converte a coluna "Data" para datetime
df['Data'] = pd.to_datetime(df['Data'])

# Cria uma nova coluna com o mês (ano+mês)
df['Ano-Mês'] = df['Data'].dt.to_period('M')

# Agrupa por mês e companhia, somando passageiros
mensal = df.groupby(['Ano-Mês', 'Companhia'])['Passageiros'].sum().reset_index()

# Converte 'Ano-Mês' para string para facilitar visualizações
mensal['Ano-Mês'] = mensal['Ano-Mês'].astype(str)

print(mensal.head())

#📊 Visualização (usando matplotlib ou seaborn):
plt.figure(figsize=(12,6))
sns.lineplot(data=mensal, x='Ano-Mês', y='Passageiros', hue='Companhia', marker='o')
plt.xticks(rotation=45)
plt.title('Evolução mensal do número de passageiros por companhia')
plt.ylabel('Total de Passageiros')
plt.xlabel('Ano-Mês')
plt.tight_layout()
plt.show()