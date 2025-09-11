import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import math
from scipy.stats import chisquare

# 1. CRIAR DADOS HISTÓRICOS SIMULADOS DA MEGA-SENA
# ===============================================
print("=" * 70)
print("📊 ANÁLISE HISTÓRICA DA MEGA-SENA")
print("=" * 70)

# Criando dados históricos simulados (3000 concursos)
np.random.seed(42)
n_concursos = 3000
dados = []

print("🎲 Gerando dados históricos simulados...")
for concurso in range(1, n_concursos + 1):
    # Gera 6 números únicos entre 1 e 60
    numeros = sorted(np.random.choice(range(1, 61), size=6, replace=False))
    dados.append([concurso] + numeros)

# Criar DataFrame
colunas = ['Concurso', 'Bola1', 'Bola2', 'Bola3', 'Bola4', 'Bola5', 'Bola6']
dados_historicos = pd.DataFrame(dados, columns=colunas)

print(f"✅ Dados simulados criados! Total de concursos: {len(dados_historicos)}")

# 2. PROCESSAR OS DADOS
# ===============================================
print("\n" + "=" * 70)
print("🔍 PROCESSANDO DADOS")
print("=" * 70)

# Coletar todos os números sorteados
todos_numeros = []
for coluna in ['Bola1', 'Bola2', 'Bola3', 'Bola4', 'Bola5', 'Bola6']:
    todos_numeros.extend(dados_historicos[coluna].values)

# Contar frequência de cada número
frequencia_numeros = Counter(todos_numeros)
numeros_ordenados = sorted(frequencia_numeros.items(), key=lambda x: x[1])

# Calcular estatísticas
total_sorteados = len(todos_numeros)
numeros_unicos = list(range(1, 61))
frequencia_media = total_sorteados / 60

print(f"📈 Estatísticas:")
print(f"   • Total de números sorteados: {total_sorteados:,}")
print(f"   • Números únicos: 1 a 60")
print(f"   • Frequência média por número: {frequencia_media:.1f} vezes")

# 3. CLASSIFICAR OS NÚMEROS
# ===============================================
print("\n" + "=" * 70)
print("🏷️  CLASSIFICANDO NÚMEROS")
print("=" * 70)

# Números mais sorteados (top 6)
mais_sorteados = [num for num, freq in numeros_ordenados[-6:]]
freq_mais_sorteados = [freq for num, freq in numeros_ordenados[-6:]]

# Números menos sorteados (bottom 6)
menos_sorteados = [num for num, freq in numeros_ordenados[:6]]
freq_menos_sorteados = [freq for num, freq in numeros_ordenados[:6]]

# Números na média (próximos da média)
numeros_media = []
for num in range(1, 61):
    freq = frequencia_numeros[num]
    if abs(freq - frequencia_media) <= frequencia_media * 0.2:  # ±20% da média
        numeros_media.append((num, freq))

# Pegar 6 números mais próximos da média
numeros_media.sort(key=lambda x: abs(x[1] - frequencia_media))
jogo_media = [num for num, freq in numeros_media[:6]]
freq_media = [freq for num, freq in numeros_media[:6]]

print("🎯 NÚMEROS MAIS SORTEADOS (Top 6):")
for i, (num, freq) in enumerate(zip(mais_sorteados, freq_mais_sorteados), 1):
    print(f"   {i}. Número {num:2d} - {freq:3d} vezes")

print(f"\n❌ NÚMEROS MENOS SORTEADOS (Bottom 6):")
for i, (num, freq) in enumerate(zip(menos_sorteados, freq_menos_sorteados), 1):
    print(f"   {i}. Número {num:2d} - {freq:3d} vezes")

print(f"\n📊 NÚMEROS NA MÉDIA (6 mais próximos):")
for i, (num, freq) in enumerate(zip(jogo_media, freq_media), 1):
    print(f"   {i}. Número {num:2d} - {freq:3d} vezes (média: {frequencia_media:.1f})")

# 4. CRIAR JOGOS SUGERIDOS
# ===============================================
print("\n" + "=" * 70)
print("🎰 JOGOS SUGERIDOS")
print("=" * 70)

jogo_mais_sorteado = sorted(mais_sorteados)
jogo_menos_sorteado = sorted(menos_sorteados)
jogo_media_sorteado = sorted(jogo_media)

print("🔥 JOGO COM NÚMEROS MAIS SORTEADOS:")
print(f"   {jogo_mais_sorteado}")

print(f"\n🧊 JOGO COM NÚMEROS MENOS SORTEADOS:")
print(f"   {jogo_menos_sorteado}")

print(f"\n⚖️  JOGO COM NÚMEROS NA MÉDIA:")
print(f"   {jogo_media_sorteado}")

# 5. VISUALIZAÇÃO GRÁFICA
# ===============================================
print("\n" + "=" * 70)
print("📊 VISUALIZAÇÃO GRÁFICA")
print("=" * 70)

plt.figure(figsize=(15, 10))

# Gráfico 1: Frequência de todos os números
plt.subplot(2, 2, 1)
numeros = list(range(1, 61))
frequencias = [frequencia_numeros[num] for num in numeros]

plt.bar(numeros, frequencias, alpha=0.7, color='skyblue')
plt.axhline(frequencia_media, color='red', linestyle='--', label=f'Média: {frequencia_media:.1f}')
plt.xlabel('Número')
plt.ylabel('Frequência')
plt.title('Frequência de Sorteio de Cada Número\nMega-Sena Histórica')
plt.legend()
plt.grid(True, alpha=0.3)

# Gráfico 2: Comparação dos três jogos sugeridos
plt.subplot(2, 2, 2)
categorias = ['Mais Sorteados', 'Na Média', 'Menos Sorteados']
medias_frequencias = [
    np.mean(freq_mais_sorteados),
    np.mean(freq_media),
    np.mean(freq_menos_sorteados)
]

bars = plt.bar(categorias, medias_frequencias, 
              color=['green', 'blue', 'red'], alpha=0.7)
plt.axhline(frequencia_media, color='red', linestyle='--', alpha=0.5)
plt.ylabel('Frequência Média')
plt.title('Frequência Média dos Jogos Sugeridos')
plt.grid(True, alpha=0.3)

# Adicionar valores nas barras
for bar, valor in zip(bars, medias_frequencias):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, 
             f'{valor:.1f}', ha='center', fontweight='bold')

# Gráfico 3: Distribuição dos números mais e menos sorteados
plt.subplot(2, 2, 3)
x_pos = range(6)
plt.bar(x_pos, freq_mais_sorteados, alpha=0.7, label='Mais Sorteados', color='green')
plt.bar(x_pos, freq_menos_sorteados, alpha=0.7, label='Menos Sorteados', color='red')
plt.axhline(frequencia_media, color='black', linestyle='--', label='Média')
plt.xticks(x_pos, [f'Nº {n}' for n in range(1, 7)])
plt.ylabel('Frequência')
plt.title('Comparação Direta: Mais vs Menos Sorteados')
plt.legend()
plt.grid(True, alpha=0.3)

# Gráfico 4: Distribuição de frequências
plt.subplot(2, 2, 4)
plt.hist(frequencias, bins=15, alpha=0.7, color='purple', edgecolor='black')
plt.axvline(frequencia_media, color='red', linestyle='--', label=f'Média: {frequencia_media:.1f}')
plt.xlabel('Frequência')
plt.ylabel('Quantidade de Números')
plt.title('Distribuição das Frequências')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# 6. ANÁLISE ESTATÍSTICA AVANÇADA
# ===============================================
print("\n" + "=" * 70)
print("📈 ANÁLISE ESTATÍSTICA AVANÇADA")
print("=" * 70)

# Calcular desvio padrão
frequencias = list(frequencia_numeros.values())
desvio_padrao = np.std(frequencias)

print("📊 ESTATÍSTICAS DE DISTRIBUIÇÃO:")
print(f"   • Média: {frequencia_media:.2f}")
print(f"   • Desvio Padrão: {desvio_padrao:.2f}")
print(f"   • Coeficiente de Variação: {(desvio_padrao/frequencia_media)*100:.1f}%")
print(f"   • Número mais sorteado: {max(frequencia_numeros, key=frequencia_numeros.get)}")
print(f"   • Número menos sorteado: {min(frequencia_numeros, key=frequencia_numeros.get)}")

# Teste de aleatoriedade (simplificado)
try:
    chi2, p_value = chisquare(list(frequencia_numeros.values()))
    print(f"\n🎲 TESTE DE ALEATORIEDADE (Qui-quadrado):")
    print(f"   • Estatística Chi²: {chi2:.2f}")
    print(f"   • p-value: {p_value:.4f}")
    print(f"   • Interpretação: {'Distribuição uniforme' if p_value > 0.05 else 'Possível viés'}")
except:
    print("\n🎲 Teste de qui-quadrado não disponível")

# 7. RECOMENDAÇÕES E CONSIDERAÇÕES
# ===============================================
print("\n" + "=" * 70)
print("💡 RECOMENDAÇÕES E CONSIDERAÇÕES")
print("=" * 70)

print("🎯 ESTRATÉGIAS DE JOGO:")
print("1. 🔥 Números Quentes: Jogue os mais sorteados (tendência continuar)")
print("2. 🧊 Números Frios: Jogue os menos sorteados ('devem' sair)")
print("3. ⚖️  Números Balanceados: Mistura de estratégias")

print(f"\n⚠️  LEMBRETE IMPORTANTE:")
print("   • Loteria é ALEATÓRIA - não há garantias!")
print("   • Probabilidade de acerto: 1 em 50.063.860")
print("   • Jogue com responsabilidade!")
print("   • Estatísticas não garantem vitória!")

print(f"\n🎲 SEUS JOGOS SUGERIDOS:")
print(f"   🔥 Quentes:   {jogo_mais_sorteado}")
print(f"   🧊 Frios:     {jogo_menos_sorteado}")
print(f"   ⚖️  Balanceado: {jogo_media_sorteado}")

# 8. EXPORTAR RESULTADOS
# ===============================================
print("\n" + "=" * 70)
print("💾 EXPORTANDO RESULTADOS")
print("=" * 70)

# Criar DataFrame com estatísticas
df_estatisticas = pd.DataFrame({
    'Número': range(1, 61),
    'Frequência': [frequencia_numeros[i] for i in range(1, 61)],
    'Desvio_Media': [abs(frequencia_numeros[i] - frequencia_media) for i in range(1, 61)],
    'Categoria': ['Quente' if i in mais_sorteados else 
                 'Frio' if i in menos_sorteados else 
                 'Médio' for i in range(1, 61)]
})

# Salvar em CSV
df_estatisticas.to_csv('estatisticas_mega_sena.csv', index=False)
print("✅ Estatísticas salvas em 'estatisticas_mega_sena.csv'")

print("\n" + "=" * 70)
print("🎯 ANÁLISE CONCLUÍDA!")
print("=" * 70)