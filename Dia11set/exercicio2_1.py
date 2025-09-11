import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# 1. ESPAÇO AMOSTRAL - DEFINIÇÃO TEÓRICA
# ===============================================
print("=" * 50)
print("ESPAÇO AMOSTRAL - 2 LANÇAMENTOS DE MOEDA")
print("=" * 50)

# Definindo os possíveis resultados do espaço amostral
# C = Coroa, K = Cara
# CC = Duas coroas, CK = Coroa then Cara, etc.
resultados_possiveis = ['CC', 'CK', 'KC', 'KK']

# Probabilidade teórica: cada um dos 4 resultados tem probabilidade 1/4 = 0.25
# Isso porque os lançamentos são independentes e a moeda é justa (p=0.5 para cada lado)
probabilidade_teorica = 1/4

print("Espaço amostral completo:")
for i, resultado in enumerate(resultados_possiveis, 1):
    print(f"{i}. {resultado}")

print(f"\nProbabilidade teórica de cada resultado: {probabilidade_teorica:.3f} (25%)")

# 2. SIMULAÇÃO DE LANÇAMENTOS - LEI DOS GRANDES NÚMEROS
# ===============================================
print("\n" + "=" * 50)
print("SIMULAÇÃO DE 10.000 LANÇAMENTOS")
print("=" * 50)

# Semente para reproducibilidade - garante que os resultados sejam os mesmos toda vez
np.random.seed(42)

# Número de experimentos - quanto maior, melhor a aproximação pela Lei dos Grandes Números
n_lancamentos = 10000

# Simulando o primeiro lançamento de moeda para todos os experimentos
# choice() seleciona aleatoriamente entre ['C', 'K'] com probabilidades iguais [0.5, 0.5]
lancamento1 = np.random.choice(['C', 'K'], size=n_lancamentos, p=[0.5, 0.5])

# Simulando o segundo lançamento de moeda (independente do primeiro)
lancamento2 = np.random.choice(['C', 'K'], size=n_lancamentos, p=[0.5, 0.5])

# Combinando os resultados dos dois lançamentos em pares
# zip() combina elementos das duas listas na mesma posição
# List comprehension cria strings como 'CC', 'CK', etc.
resultados_simulados = [f"{l1}{l2}" for l1, l2 in zip(lancamento1, lancamento2)]

# 3. ANÁLISE DE FREQUÊNCIAS EMPÍRICAS
# ===============================================
# Usando Counter para contar quantas vezes cada resultado ocorreu
contagem = Counter(resultados_simulados)

# Convertendo contagens absolutas em frequências relativas (probabilidades empíricas)
# Frequência empírica = número de ocorrências / total de experimentos
frequencias_empiricas = {resultado: count/n_lancamentos for resultado, count in contagem.items()}

print("Frequências empíricas encontradas:")
for resultado in resultados_possiveis:
    freq_empirica = frequencias_empiricas.get(resultado, 0)
    print(f"{resultado}: {freq_empirica:.4f} ({freq_empirica*100:.1f}%)")

# 4. COMPARAÇÃO ENTRE TEÓRICO E EMPÍRICO
# ===============================================
print("\n" + "=" * 50)
print("COMPARAÇÃO: TEÓRICO vs EMPÍRICO")
print("=" * 50)

print("Resultado | Teórico | Empírico  | Diferença")
print("-" * 40)

# Para cada resultado possível, comparamos a probabilidade teórica com a empírica
for resultado in resultados_possiveis:
    teorico = 0.25  # Valor teórico esperado
    empirico = frequencias_empiricas.get(resultado, 0)  # Valor observado
    diferenca = abs(teorico - empirico)  # Diferença absoluta
    print(f"{resultado:^9} | {teorico:.4f}  | {empirico:.4f}   | {diferenca:.4f}")

# 5. VISUALIZAÇÃO GRÁFICA - COMPARAÇÃO VISUAL
# ===============================================
plt.figure(figsize=(12, 6))

# Preparando dados para o gráfico de barras
resultados = resultados_possiveis
teoricos = [0.25] * 4  # Lista com 4 valores 0.25 (um para cada resultado)
empiricos = [frequencias_empiricas.get(r, 0) for r in resultados]  # Frequências observadas

# Posições no eixo X para as barras
x_pos = np.arange(len(resultados))
largura = 0.35  # Largura das barras

# Criando barras para probabilidades teóricas (azul)
plt.bar(x_pos - largura/2, teoricos, largura, label='Teórico', alpha=0.8, color='green')

# Criando barras para probabilidades empíricas (vermelho)
plt.bar(x_pos + largura/2, empiricos, largura, label='Empírico', alpha=0.8, color='orange')

# Configurações do gráfico
plt.xlabel('Resultados')
plt.ylabel('Probabilidade')
plt.title('Comparação: Probabilidades Teóricas vs Empíricas\n(10.000 lançamentos de 2 moedas)')
plt.xticks(x_pos, resultados)
plt.legend()
plt.grid(True, alpha=0.3)

# Adicionando valores numéricos sobre as barras para melhor leitura
for i, (teorico, empirico) in enumerate(zip(teoricos, empiricos)):
    plt.text(i - largura/2, teorico + 0.01, f'{teorico:.3f}', ha='center')
    plt.text(i + largura/2, empirico + 0.01, f'{empirico:.3f}', ha='center')

plt.tight_layout()
plt.show()

# 6. ANÁLISE ESTATÍSTICA - QUANTIFICANDO A APROXIMAÇÃO
# ===============================================
print("\n" + "=" * 50)
print("ANÁLISE ESTATÍSTICA")
print("=" * 50)

# Calculando a diferença média absoluta entre teórico e empírico
# Para cada resultado, calculamos |teórico - empírico| e tiramos a média
diferenca_media = np.mean([abs(0.25 - frequencias_empiricas.get(r, 0)) for r in resultados_possiveis])

# Calculando o erro percentual médio em relação ao valor teórico
erro_percentual = diferenca_media/0.25*100

print(f"Diferença média absoluta: {diferenca_media:.6f}")
print(f"Erro percentual médio: {erro_percentual:.2f}%")

# Conclusão baseada na Lei dos Grandes Números
print(f"\nTotal de lançamentos simulados: {n_lancamentos:,}")
print("As frequências empíricas se aproximam das probabilidades teóricas!")
print("   Isso demonstra a Lei dos Grandes Números em ação!")