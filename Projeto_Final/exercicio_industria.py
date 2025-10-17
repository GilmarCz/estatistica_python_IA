# ======================================
# 📘 LISTA DE EXERCÍCIOS DE IA - RESOLVIDA
# Estatística, Probabilidade e Visualização com Python
# Autor: Gilmar Czeika
# Curso: Técnico em Inteligência Artificial – SENAC
# ======================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sympy import symbols, Eq, solve
from sklearn.linear_model import LinearRegression

# ------------------------------------------------------------
# 🔹 CAPÍTULO 1 – PROBABILIDADE
# ------------------------------------------------------------

print("\n===== CAPÍTULO 1 – PROBABILIDADE =====\n")

# 1. Urna com bolas coloridas
vermelhas = 5
azuis = 7
total = vermelhas + azuis
prob_vermelha = vermelhas / total
print(f"1️⃣ Probabilidade de retirar uma bola vermelha: {prob_vermelha:.2f} ({prob_vermelha*100:.1f}%)")

# 2. Lançamento de um dado
total_faces = 6
favoraveis = 3  # números maiores que 3: 4,5,6
prob_maior_3 = favoraveis / total_faces
print(f"2️⃣ Probabilidade de sair número > 3: {prob_maior_3:.2f} ({prob_maior_3*100:.1f}%)")

# 3. Lançamento de duas moedas (exatamente uma cara)
# Espaço amostral: CC, CX, XC, XX
# Casos favoráveis: CX, XC
prob_uma_cara = 2 / 4
print(f"3️⃣ Probabilidade de sair exatamente uma cara: {prob_uma_cara:.2f} ({prob_uma_cara*100:.1f}%)")

# 4. Probabilidade condicional
# 3 vermelhas e 2 verdes
# Sem reposição, primeira vermelha, qual a probabilidade da segunda ser verde?
P_vermelha_1 = 3/5
P_verde_2_dado_vermelha = 2/4
P_conjunta = P_vermelha_1 * P_verde_2_dado_vermelha
print(f"4️⃣ Probabilidade de tirar vermelha e depois verde (sem reposição): {P_conjunta:.2f}")

# ------------------------------------------------------------
# 🔹 CAPÍTULO 2 – ESTATÍSTICA DESCRITIVA COM PANDAS
# ------------------------------------------------------------

print("\n===== CAPÍTULO 2 – ESTATÍSTICA DESCRITIVA =====\n")

# 5. Média, mediana e moda
dados = pd.Series([10, 15, 20, 20, 25, 30, 35])
print("5️⃣ Média:", dados.mean())
print("   Mediana:", dados.median())
print("   Moda:", dados.mode()[0])

# 6. Variância e desvio padrão
dados2 = pd.Series([2, 4, 4, 4, 5, 5, 7, 9])
print("6️⃣ Variância:", dados2.var())
print("   Desvio padrão:", dados2.std())

# 7. Medidas resumo
dados3 = pd.Series([5, 7, 8, 5, 10, 12, 15])
print("7️⃣ Média:", dados3.mean())
print("   Mediana:", dados3.median())
print("   Valor mínimo:", dados3.min())
print("   Valor máximo:", dados3.max())
print("   Amplitude:", dados3.max() - dados3.min())

# ------------------------------------------------------------
# 🔹 CAPÍTULO 3 – FUNÇÕES TRIGONOMÉTRICAS E LOGARÍTMICAS
# ------------------------------------------------------------

print("\n===== CAPÍTULO 3 – FUNÇÕES TRIGONOMÉTRICAS E LOGARÍTMICAS =====\n")

x = np.linspace(0.1, 10, 100)
y = np.sin(x) + np.log(x)
plt.figure(figsize=(8,5))
plt.plot(x, y, color='blue', linewidth=2)
plt.title("Função y = sin(x) + log(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

# ------------------------------------------------------------
# 🔹 CAPÍTULO 4 – REGRESSÃO LINEAR
# ------------------------------------------------------------

print("\n===== CAPÍTULO 4 – REGRESSÃO LINEAR =====\n")

# 9. Horas de estudo vs. notas
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 5, 4, 6])
modelo = LinearRegression().fit(X, y)
coef = modelo.coef_[0]
intercepto = modelo.intercept_
print(f"9️⃣ Coeficiente angular (inclinação): {coef:.2f}")
print(f"   Intercepto: {intercepto:.2f}")

# 10. Preço vs. tamanho de imóveis
X2 = np.array([50, 60, 70, 80, 90]).reshape(-1, 1)
y2 = np.array([150, 200, 210, 240, 280])
modelo2 = LinearRegression().fit(X2, y2)
preco_previsto = modelo2.predict([[100]])[0]
print(f"🔟 Preço estimado para imóvel de 100 m²: {preco_previsto:.2f} mil reais")

plt.figure(figsize=(8,5))
plt.scatter(X2, y2, color='blue', label='Dados reais')
plt.plot(X2, modelo2.predict(X2), color='red', label='Regressão Linear')
plt.xlabel("Tamanho (m²)")
plt.ylabel("Preço (mil R$)")
plt.title("Preço vs. Tamanho do Imóvel")
plt.legend()
plt.show()

# ------------------------------------------------------------
# 🔹 CAPÍTULO 5 – VISUALIZAÇÕES COM MATPLOTLIB E SEABORN
# ------------------------------------------------------------

print("\n===== CAPÍTULO 5 – VISUALIZAÇÕES =====\n")

# 11. Histograma com Matplotlib e Seaborn
dados_normais = np.random.normal(60, 15, 1000)

plt.figure(figsize=(7,4))
plt.hist(dados_normais, bins=20, color='lightblue', edgecolor='black')
plt.title("Histograma - Matplotlib")
plt.xlabel("Valores")
plt.ylabel("Frequência")
plt.show()

sns.histplot(dados_normais, bins=20, kde=True, color='skyblue')
plt.title("Histograma - Seaborn")
plt.xlabel("Valores")
plt.ylabel("Frequência")
plt.show()

# 12. Gráfico de dispersão (Seaborn)
X = [1, 2, 3, 4, 5]
Y = [2, 4, 5, 4, 6]
sns.scatterplot(x=X, y=Y, color='red', s=100)
plt.title("Gráfico de Dispersão - Seaborn")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# 13. Boxplot (Seaborn)
dados_box = [7, 8, 5, 6, 12, 14, 15, 8, 9, 10]
sns.boxplot(data=dados_box, color='lightgreen')
plt.title("Boxplot - Distribuição dos Dados")
plt.show()

# 14. Exercício final (industria.csv)
# -> Exemplo genérico de leitura
print("\n14️⃣ Exemplo de leitura de arquivo CSV:")
print("df = pd.read_csv('industria.csv')")
print("df.head()")
print("df.describe()")


# ================================================================
# EXERCÍCIO 14 – ANÁLISE DO ARQUIVO industria.csv
# ================================================================

# Carregar o arquivo CSV
df = pd.read_csv("industria.csv")

print("\nPrimeiras linhas do arquivo:")
print(df.head())

print("\nInformações gerais:")
print(df.info())

# ================================================================
# EXERCÍCIO 1 – Receita total por fábrica
# ================================================================

receita_fabrica = df.groupby("Fabrica")["Receita"].sum().sort_values(ascending=False)
print("\nReceita total por fábrica:\n", receita_fabrica)

# Gráfico de barras
plt.figure(figsize=(8,5))
sns.barplot(x=receita_fabrica.index, y=receita_fabrica.values, palette="viridis")
plt.title("Receita Total por Fábrica")
plt.ylabel("Receita Total (R$)")
plt.xlabel("Fábrica")
plt.tight_layout()
plt.show()

# Perguntas:
fabrica_maior = receita_fabrica.idxmax()
fabrica_menor = receita_fabrica.idxmin()
dif_receita = receita_fabrica.max() - receita_fabrica.min()
print(f"Fábrica com maior receita: {fabrica_maior}")
print(f"Diferença entre maior e menor receita: R$ {dif_receita:,.2f}")

# ================================================================
# EXERCÍCIO 2 – Receita média por produto
# ================================================================

receita_media_produto = df.groupby("Produto")["Receita"].mean().sort_values(ascending=False)
print("\nReceita média por produto:\n", receita_media_produto)

plt.figure(figsize=(8,5))
sns.barplot(x=receita_media_produto.index, y=receita_media_produto.values, palette="coolwarm")
plt.title("Receita Média por Produto")
plt.ylabel("Receita Média (R$)")
plt.xlabel("Produto")
plt.tight_layout()
plt.show()

print(f"Produto com maior receita média: {receita_media_produto.idxmax()}")

# ================================================================
# EXERCÍCIO 3 – Quantidade vendida total por mês
# ================================================================

# Converter datas
df["Data"] = pd.to_datetime(df["Data"], errors="coerce")
df["Mes"] = df["Data"].dt.to_period("M").astype(str)

vendas_mes = df.groupby("Mes")["Quantidade_Vendida"].sum()

plt.figure(figsize=(10,5))
sns.lineplot(x=vendas_mes.index, y=vendas_mes.values, marker="o", color="green")
plt.title("Quantidade Total Vendida por Mês")
plt.ylabel("Quantidade Total")
plt.xlabel("Mês")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

mes_mais_vendas = vendas_mes.idxmax()
print(f"Mês com maior quantidade vendida: {mes_mais_vendas}")

# ================================================================
# EXERCÍCIO 4 – Lucro médio por fábrica
# ================================================================

df["Lucro"] = df["Receita"] - df["Custo"]
lucro_medio = df.groupby("Fabrica")["Lucro"].mean().sort_values(ascending=False)
print("\nLucro médio por fábrica:\n", lucro_medio)

plt.figure(figsize=(8,5))
sns.barplot(x=lucro_medio.index, y=lucro_medio.values, palette="crest")
plt.title("Lucro Médio por Fábrica")
plt.ylabel("Lucro Médio (R$)")
plt.xlabel("Fábrica")
plt.tight_layout()
plt.show()

fabrica_lucrativa = lucro_medio.idxmax()
print(f"Fábrica mais lucrativa: {fabrica_lucrativa}")

if (df["Lucro"] < 0).any():
    print("Existe pelo menos um registro com lucro negativo.")
else:
    print("Nenhuma fábrica apresentou lucro negativo.")

# ================================================================
# EXERCÍCIO 5 – Receita total por fábrica e produto
# ================================================================

tabela_receita = df.pivot_table(values="Receita", index="Fabrica", columns="Produto", aggfunc="sum", fill_value=0)
print("\nReceita total por fábrica e produto:\n", tabela_receita)

plt.figure(figsize=(8,6))
sns.heatmap(tabela_receita, annot=True, fmt=".0f", cmap="YlGnBu")
plt.title("Heatmap – Receita por Fábrica e Produto")
plt.xlabel("Produto")
plt.ylabel("Fábrica")
plt.tight_layout()
plt.show()

# Perguntas finais:
for fabrica in tabela_receita.index:
    produto_top = tabela_receita.loc[fabrica].idxmax()
    print(f"{fabrica}: produto com maior receita = {produto_top}")

print("\nAnálise concluída com sucesso!")
