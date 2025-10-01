# === IMPORTS ===
import pandas as pd               # manipulação de dados em tabelas (DataFrame)
import numpy as np                # operações numéricas
import seaborn as sns             # visualizações estatísticas (construído sobre matplotlib)
import matplotlib.pyplot as plt   # controle fino dos gráficos

# === PARTE A – CARREGAMENTO E INSPEÇÃO ===
# Lê o CSV e converte a coluna "Data" para datetime automaticamente
df = pd.read_csv("dados1.csv", parse_dates=["Data"])

# df.info() imprime no console informação sobre o DataFrame (colunas, tipos, non-null)
print("Informações do DataFrame (df.info()):")
df.info()                         # retorna None, mas imprime o resumo no stdout
print("\n")
# Mostra dimensão (linhas, colunas)
print("\nDimensão:", df.shape)

# Tipos de dados por coluna
print("\nTipos de dados:\n", df.dtypes)

# Primeiras 5 linhas para inspeção rápida
print("\nPrimeiras linhas:\n", df.head())

# Verifica valores nulos por coluna (útil para limpeza de dados)
print("\nValores nulos por coluna:\n", df.isnull().sum())

# === PARTE B – ESTATÍSTICAS DESCRITIVAS ===
# Para cada coluna numérica relevante, calculamos média, mediana, desvio padrão e variância
for col in ["Passageiros", "Distância (km)", "Ocupação (%)", "Receita (R$)"]:
    print(f"\n--- Estatísticas para '{col}' ---")
    print("Média:", df[col].mean())         # média aritmética
    print("Mediana:", df[col].median())     # percentil 50
    print("Desvio padrão:", df[col].std())  # dispersão (raiz da variância)
    print("Variância:", df[col].var())      # variância

# Percentis (quartis) para a receita: 25%, 50% (mediana), 75%
print("\nPercentis da Receita (25%, 50%, 75%):")
print(df["Receita (R$)"].quantile([0.25, 0.5, 0.75]))

# Companhia com maior receita total:
# groupby soma a 'Receita (R$)' por companhia; idxmax retorna o rótulo com o maior valor
comp_maior_receita = df.groupby("Companhia")["Receita (R$)"].sum().idxmax()
print("\nCompanhia com maior receita total:", comp_maior_receita)

# Companhia com maior número total de passageiros
comp_mais_passageiros = df.groupby("Companhia")["Passageiros"].sum().idxmax()
print("Companhia com mais passageiros:", comp_mais_passageiros)

# Contagem de voos por companhia (quantos registros/linhas por companhia)
print("\nVoos por companhia:")
print(df["Companhia"].value_counts())

# Receita média por companhia
print("\nReceita média por companhia:")
print(df.groupby("Companhia")["Receita (R$)"].mean())

# Receita média por aeroporto de origem
print("\nReceita média por aeroporto de origem:")
print(df.groupby("Aeroporto Origem")["Receita (R$)"].mean())

# === PARTE C – VISUALIZAÇÕES ===
# Histórico: distribuição de passageiros (histograma + KDE)
plt.figure()
sns.histplot(df["Passageiros"], kde=True)   # kde=True desenha uma estimativa de densidade
plt.title("Distribuição de Passageiros")
plt.xlabel("Passageiros")
plt.ylabel("Frequência")
plt.show(block=False)  # block=False mantém o script rodando (útil em notebooks/terminais interativos)

# Boxplot da ocupação por companhia (mostra mediana, quartis e possíveis outliers)
plt.figure()
sns.boxplot(x="Companhia", y="Ocupação (%)", data=df)
plt.title("Boxplot da Ocupação (%) por Companhia")
plt.xlabel("Companhia")
plt.ylabel("Ocupação (%)")
plt.show(block=False)

# Barra: receita média por companhia (estimator=np.mean calcula a média para cada grupo)
plt.figure()
sns.barplot(x="Companhia", y="Receita (R$)", data=df, estimator=np.mean, errorbar=None)
plt.title("Receita Média por Companhia")
plt.xlabel("Companhia")
plt.ylabel("Receita média (R$)")
plt.show(block=False)

# Scatter: relação entre distância e receita, colorido por companhia para ver padrões por operadora
plt.figure()
sns.scatterplot(x="Distância (km)", y="Receita (R$)", hue="Companhia", data=df)
plt.title("Distância (km) x Receita (R$)")
plt.xlabel("Distância (km)")
plt.ylabel("Receita (R$)")
plt.legend(title="Companhia")
plt.show(block=False)

# Heatmap de correlação entre variáveis numéricas — ajuda a ver forças de relação linear
plt.figure()
corr = df[["Passageiros", "Distância (km)", "Ocupação (%)", "Receita (R$)"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Mapa de Correlação (Pearson)")
plt.show(block=False)

# === PARTE D – PERGUNTAS ANALÍTICAS (COM GRÁFICOS) ===
# 1) Companhia com mais voos: usar value_counts para ordenar e idxmax para pegar a maior
comp_mais_voos = df["Companhia"].value_counts().idxmax()
print("\nCompanhia com mais voos:", comp_mais_voos)

# Gráfico: número de voos por companhia (countplot)
plt.figure()
sns.countplot(x="Companhia", data=df, order=df["Companhia"].value_counts().index)
plt.title("Número de Voos por Companhia")
plt.xlabel("Companhia")
plt.ylabel("Número de voos (contagem de registros)")
plt.show(block=False)

# 2) Verificar se distância influencia receita — usamos correlação de Pearson
corr_dist_receita = df["Distância (km)"].corr(df["Receita (R$)"])
print("\nCorrelação distância x receita:", corr_dist_receita)
# Comentário: coeficiente próximo de 0 indica pouca relação linear; próximo de 1/-1 indica relação forte.

# 3) Verificar se ocupação está relacionada à receita
corr_ocup_receita = df["Ocupação (%)"].corr(df["Receita (R$)"])
print("\nCorrelação ocupação x receita:", corr_ocup_receita)

# 4) Aeroportos de origem com mais voos (contagem)
print("\nAeroportos de origem com mais voos:")
print(df["Aeroporto Origem"].value_counts())

# Gráfico: número de voos por aeroporto de origem
plt.figure(figsize=(8,4))
sns.countplot(x="Aeroporto Origem", data=df, order=df["Aeroporto Origem"].value_counts().index)
plt.title("Número de Voos por Aeroporto de Origem")
plt.xlabel("Aeroporto Origem")
plt.ylabel("Número de voos")
plt.show(block=False)

# === EXTENSÃO ===
# Cria coluna 'Mes' (periodo mensal) para análises agregadas por mês
df["Mes"] = df["Data"].dt.to_period("M")

# Receita média por mês (agregação por período)
print("\nReceita média por mês:")
print(df.groupby("Mes")["Receita (R$)"].mean())

# Gráfico: receita média por mês (linha)
plt.figure(figsize=(8,4))
df.groupby("Mes")["Receita (R$)"].mean().plot(marker="o")
plt.title("Receita Média por Mês")
plt.xlabel("Mês")
plt.ylabel("Receita média (R$)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show(block=False)

# Ocupação média por companhia
print("\nOcupação média por companhia:")
print(df.groupby("Companhia")["Ocupação (%)"].mean())

# Gráfico: ocupação média por companhia (barra)
plt.figure()
df.groupby("Companhia")["Ocupação (%)"].mean().plot(kind="bar")
plt.title("Ocupação Média por Companhia")
plt.xlabel("Companhia")
plt.ylabel("Ocupação média (%)")
plt.show(block=False)


df.groupby(['Companhia', 'Aeroporto Origem', 'Aeroporto Destino']).agg({ 'Passageiros': 'sum', 'Receita (R$)': 'sum', 'Ocupação (%)': 'mean' }).reset_index()

# === EVOLUÇÃO MENSAL DO TOTAL DE PASSAGEIROS POR COMPANHIA ===
# Agrupa os dados por mês e companhia
passageiros_mes = (
    df.groupby(["Mes", "Companhia"])["Passageiros"]
    .sum()
    .reset_index()
)

# Converter Mes de Period para string (ex: "2023-01")
passageiros_mes["Mes"] = passageiros_mes["Mes"].astype(str)

print("\n=== Total de passageiros por mês e companhia ===")
print(passageiros_mes.head())

# Gráfico
plt.figure(figsize=(10, 6))
sns.lineplot(data=passageiros_mes, x="Mes", y="Passageiros", hue="Companhia", marker="o")
plt.title("Evolução Mensal do Total de Passageiros por Companhia")
plt.xlabel("Mês")
plt.ylabel("Total de Passageiros")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show(block=False)


# === FINALIZAÇÃO: mantém os gráficos abertos até o usuário pressionar Enter ===
# Em ambientes interativos, plt.show() já pode ser suficiente. Aqui usamos input para permitir inspeção.
input("Pressione Enter para fechar os gráficos...")
plt.close('all')



# Criar coluna "Rota"
df["Rota"] = df["Aeroporto Origem"] + " → " + df["Aeroporto Destino"]

# Receita por passageiro
df["Receita_por_Passageiro"] = df["Receita (R$)"] / df["Passageiros"]

# Agrupamento por Companhia e Rota
rotas = df.groupby(["Companhia", "Rota"]).agg({
    "Ocupação (%)": "mean",
    "Receita_por_Passageiro": "mean"
}).reset_index()

# Ordenar pelas rotas mais eficientes (receita por passageiro, descrescente)
top5_rotas = rotas.sort_values("Receita_por_Passageiro", ascending=False).head(5)

print("\n=== Top 5 Rotas mais eficientes por Receita por Passageiro ===")
print(top5_rotas)

# Garantir que Data é datetime
df["Data"] = pd.to_datetime(df["Data"])

# Criar coluna de mês (no formato AAAA-MM)
df["Mes"] = df["Data"].dt.to_period("M")

# Agrupar por mês e companhia
passageiros_mes = df.groupby(["Mes", "Companhia"])["Passageiros"].sum().reset_index()

print("\n=== Total de passageiros por mês e companhia ===")
print(passageiros_mes.head())