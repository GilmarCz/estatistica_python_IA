import pandas as pd

# Leitura do CSV
df = pd.read_csv('dados1.csv')

# Agrupamento por Companhia, Origem e Destino
grouped = df.groupby(['Companhia', 'Aeroporto Origem', 'Aeroporto Destino']).agg({
    'Passageiros': 'sum',
    'Receita (R$)': 'sum',
    'Ocupação (%)': 'mean'
}).reset_index()

# Formato do Novo Dataframe 
print("O FORMATO DO NOVO DATAFRAME APÓS O AGRUPAMENTO É:")
print(grouped)

# Nova coluna: Receita média por passageiro
grouped['Receita por Passageiro'] = grouped['Receita (R$)'] / grouped['Passageiros']

# Ordenar para ver as melhores rotas
melhores_rotas = grouped.sort_values(by='Receita por Passageiro', ascending=False)

print("AS CINCO MELHORES ROTAS ORDENADAS POR RECEITAS POR PASSAGEIRO SÃO: ")
print(melhores_rotas.head())
