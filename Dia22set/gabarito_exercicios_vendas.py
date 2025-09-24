import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# === PARTE 1 – CARREGAMENTO E INSPEÇÃO ===
df = pd.read_csv("dados.csv", parse_dates=["Data"])

print("\nDimensão do DataFrame:", df.shape)
print("\nTipos de dados:\n", df.dtypes)
print("\n5 primeiras linhas:\n", df.head())
print("\nValores nulos por coluna:\n", df.isnull().sum())

# === PARTE 2 – ESTATÍSTICAS DESCRITIVAS ===
for col in ["Vendas", "Preço Unitário", "Receita Total"]:
    print(f"\n--- Estatísticas para {col} ---")
    print("Média:", df[col].mean())
    print("Mediana:", df[col].median())
    print("Desvio padrão:", df[col].std())
    print("Variância:", df[col].var())

print("\nPercentis da Receita Total:")
print(df["Receita Total"].quantile([0.25, 0.5, 0.75]))

# Produto com maior receita total
produto_maior_receita = df.groupby("Produto")["Receita Total"].sum().idxmax()
print("\nProduto com maior receita total:", produto_maior_receita)

# Região com maior volume de vendas
regiao_maior_venda = df.groupby("Região")["Vendas"].sum().idxmax()
print("Região com maior volume de vendas:", regiao_maior_venda)

# Quantidade de registros por produto
print("\nQuantidade de registros por produto:")
print(df["Produto"].value_counts())

# Receita média por produto e por região
print("\nReceita média por produto:")
print(df.groupby("Produto")["Receita Total"].mean())
print("\nReceita média por região:")
print(df.groupby("Região")["Receita Total"].mean())

# === PARTE 3 – VISUALIZAÇÕES ===
plt.figure()
sns.histplot(df["Vendas"], kde=True)
plt.title("Histograma de Vendas")
plt.show(block=False)

plt.figure()
sns.boxplot(x="Região", y="Receita Total", data=df)
plt.title("Boxplot de Receita Total por Região")
plt.show(block=False)

plt.figure()
sns.barplot(x="Produto", y="Receita Total", data=df, estimator=np.mean, errorbar=None)
plt.title("Receita Média por Produto")
plt.show(block=False)

plt.figure()
sns.scatterplot(x="Vendas", y="Receita Total", hue="Produto", data=df)
plt.title("Relação entre Vendas e Receita Total")
plt.show(block=False)

plt.figure()
sns.heatmap(df[["Vendas", "Preço Unitário", "Receita Total"]].corr(), annot=True, cmap="coolwarm")
plt.title("Mapa de Correlação")
plt.show(block=False)
input("Pressione Enter para fechar tudo...")
plt.close('all')

# === PARTE 4 – INTERPRETAÇÃO ===
# As respostas aqui são abertas; o professor pode pedir para os alunos escreverem no notebook ou em relatório.