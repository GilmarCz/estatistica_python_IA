import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Lendo o arquivo (substitua pelo nome do seu CSV)
df = pd.read_csv("dados1.csv")

# Converter coluna Data para datetime
df["Data"] = pd.to_datetime(df["Data"])

# Criar coluna com o mês/ano
df["Mes"] = df["Data"].dt.to_period("M")

# 1) Receita média por mês
receita_media_mes = df.groupby("Mes")["Receita (R$)"].mean().reset_index()

# 2) Ocupação média por companhia
ocupacao_media_companhia = df.groupby("Companhia")["Ocupação (%)"].mean().reset_index()

print("Receita média por mês:")
print(receita_media_mes)
print("\nOcupação média por companhia:")
print(ocupacao_media_companhia)

# Extrair o mês
df['Mes'] = df['Data'].dt.to_period('M')
# Receita média por mês
receita_mes = df.groupby('Mes')['Receita (R$)'].mean().reset_index()
receita_mes['Mes_str'] = receita_mes['Mes'].astype(str)  # Para usar como hue

# Gráfico de Receita Média por Mês
plt.figure(figsize=(10,5))
sns.barplot(
    data=receita_mes, 
    x='Mes_str', 
    y='Receita (R$)', 
    hue='Mes_str',         # Hue para evitar warning
    palette='viridis', 
    dodge=False, 
    legend=False
)
plt.title("Receita Média por Mês")
plt.ylabel("Receita Média (R$)")
plt.xlabel("Mês")
plt.xticks(rotation=45)
plt.show()

grouped = df.groupby(['Companhia', 'Aeroporto Origem', 'Aeroporto Destino']).agg({
    'Passageiros': 'sum',
    'Receita (R$)': 'sum',
    'Ocupação (%)': 'mean'
}).reset_index()
