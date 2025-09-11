import numpy as np
import matplotlib.pyplot as plt
import math

# 1. CÁLCULO DAS PROBABILIDADES TEÓRICAS
# ===============================================
print("=" * 70)
print("🎰 COMPARAÇÃO: MEGA-SENA vs MEGA DA VIRADA")
print("=" * 70)

# Função para calcular combinações (n choose k)
def combinacao(n, k):
    return math.comb(n, k)

# Probabilidade da Mega-Sena (6 números entre 60)
numeros_mega = 60
escolher_mega = 6
combinacoes_mega = combinacao(numeros_mega, escolher_mega)
probabilidade_mega = 1 / combinacoes_mega

# Probabilidade da Mega da Virada (6 números entre 50 + 2 estrelas entre 5)
numeros_virada = 50
escolher_virada = 6
estrelas_virada = 5
escolher_estrelas = 2

combinacoes_numeros = combinacao(numeros_virada, escolher_virada)
combinacoes_estrelas = combinacao(estrelas_virada, escolher_estrelas)
combinacoes_total_virada = combinacoes_numeros * combinacoes_estrelas
probabilidade_virada = 1 / combinacoes_total_virada

print("📊 PROBABILIDADES TEÓRICAS:")
print(f"🎯 MEGA-SENA: 1 chance em {combinacoes_mega:,}")
print(f"   → Probabilidade: {probabilidade_mega:.15f}")
print(f"   → Notação científica: {probabilidade_mega:.2e}")

print(f"\n🎄 MEGA DA VIRADA: 1 chance em {combinacoes_total_virada:,}")
print(f"   → Probabilidade: {probabilidade_virada:.15f}")
print(f"   → Notação científica: {probabilidade_virada:.2e}")

# 2. COMPARAÇÃO RELATIVA
# ===============================================
print("\n" + "=" * 70)
print("📈 COMPARAÇÃO RELATIVA")
print("=" * 70)

razao = probabilidade_mega / probabilidade_virada
diferenca_ordem_magnitude = math.log10(probabilidade_mega) - math.log10(probabilidade_virada)

print(f"🔍 A Mega-Sena é {razao:,.1f} vezes MAIS PROVÁVEL que a Mega da Virada!")
print(f"📏 Diferença de {abs(diferenca_ordem_magnitude):.1f} ordens de magnitude")

# 3. SIMULAÇÃO (LEI DOS GRANDES NÚMEROS)
# ===============================================
print("\n" + "=" * 70)
print("🎲 SIMULAÇÃO - LEI DOS GRANDES NÚMEROS")
print("=" * 70)

np.random.seed(42)
n_simulacoes = 1000000  # 1 milhão de tentativas

print(f"Simulando {n_simulacoes:,} tentativas de cada loteria...")

# Simulação Mega-Sena
acertos_mega = 0
for i in range(n_simulacoes):
    # Gera jogo sorteado (6 números entre 1-60)
    sorteado_mega = np.random.choice(range(1, 61), size=6, replace=False)
    # Gera jogo do apostador
    aposta_mega = np.random.choice(range(1, 61), size=6, replace=False)
    # Verifica se acertou todos os números
    if set(aposta_mega) == set(sorteado_mega):
        acertos_mega += 1

prob_empirica_mega = acertos_mega / n_simulacoes

# Simulação Mega da Virada (simplificada - apenas os números principais)
acertos_virada = 0
for i in range(n_simulacoes):
    # Gera jogo sorteado (6 números entre 1-50)
    sorteado_virada = np.random.choice(range(1, 51), size=6, replace=False)
    # Gera jogo do apostador
    aposta_virada = np.random.choice(range(1, 51), size=6, replace=False)
    # Verifica se acertou todos os números (ignorando estrelas para simplificar)
    if set(aposta_virada) == set(sorteado_virada):
        acertos_virada += 1

prob_empirica_virada = acertos_virada / n_simulacoes

print(f"✅ Mega-Sena - Acertos: {acertos_mega} → Probabilidade: {prob_empirica_mega:.8f}")
print(f"✅ Mega Virada - Acertos: {acertos_virada} → Probabilidade: {prob_empirica_virada:.8f}")

# 4. VISUALIZAÇÃO GRÁFICA
# ===============================================
print("\n" + "=" * 70)
print("📊 VISUALIZAÇÃO GRÁFICA")
print("=" * 70)

plt.figure(figsize=(15, 10))

# Gráfico 1: Comparação de probabilidades
plt.subplot(2, 2, 1)
loterias = ['Mega-Sena', 'Mega da Virada']
probabilidades = [probabilidade_mega, probabilidade_virada]

bars = plt.bar(loterias, probabilidades, color=['blue', 'red'], alpha=0.7)
plt.ylabel('Probabilidade')
plt.title('Comparação de Probabilidades\n(Escala Linear)')
plt.yscale('log')  # Escala logarítmica para melhor visualização

# Adicionar valores nas barras
for bar, prob in zip(bars, probabilidades):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height, f'{prob:.1e}', 
             ha='center', va='bottom', fontweight='bold')

# Gráfico 2: Comparação em escala logarítmica
plt.subplot(2, 2, 2)
plt.bar(loterias, probabilidades, color=['blue', 'red'], alpha=0.7)
plt.ylabel('Probabilidade (log)')
plt.title('Comparação em Escala Logarítmica')
plt.yscale('log')

# Gráfico 3: Número de combinações possíveis
plt.subplot(2, 2, 3)
combinacoes = [combinacoes_mega, combinacoes_total_virada]
bars = plt.bar(loterias, combinacoes, color=['lightblue', 'lightcoral'], alpha=0.7)
plt.ylabel('Número de Combinações')
plt.title('Combinações Possíveis')
plt.yscale('log')

# Adicionar valores nas barras
for bar, comb in zip(bars, combinacoes):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height, f'{comb:,}', 
             ha='center', va='bottom', fontweight='bold', fontsize=8)

# Gráfico 4: Analogias para entender as probabilidades
plt.subplot(2, 2, 4)
analogias = [
    "Chance de ser atingido\npor um raio",
    "Mega-Sena",
    "Mega da Virada"
]
chances = [1/1500000, probabilidade_mega, probabilidade_virada]

plt.bar(analogias, chances, color=['gray', 'blue', 'red'], alpha=0.7)
plt.ylabel('Probabilidade')
plt.title('Comparação com Analogias')
plt.yscale('log')
plt.xticks(rotation=15)

plt.tight_layout()
plt.show()

# 5. ANÁLISE ESTATÍSTICA DETALHADA
# ===============================================
print("\n" + "=" * 70)
print("📋 ANÁLISE ESTATÍSTICA DETALHADA")
print("=" * 70)

print("🎯 MEGA-SENA:")
print(f"   • Combinações possíveis: {combinacoes_mega:,}")
print(f"   • Probabilidade: 1 em {combinacoes_mega:,}")
print(f"   • Notação científica: {probabilidade_mega:.2e}")

print(f"\n🎄 MEGA DA VIRADA:")
print(f"   • Combinações de números: {combinacoes_numeros:,}")
print(f"   • Combinações de estrelas: {combinacoes_estrelas:,}")
print(f"   • Total combinações: {combinacoes_total_virada:,}")
print(f"   • Probabilidade: 1 em {combinacoes_total_virada:,}")
print(f"   • Notação científica: {probabilidade_virada:.2e}")

print(f"\n⚖️  COMPARAÇÃO:")
print(f"   • Razão Mega-Sena/Mega-Virada: {razao:,.1f}×")
print(f"   • A Mega-Sena é {razao:,.0f} vezes mais provável!")

# 6. PERSPECTIVAS PRÁTICAS
# ===============================================
print("\n" + "=" * 70)
print("💡 PERSPECTIVAS PRÁTICAS")
print("=" * 70)

# Quantos anos levaria para apostar todas as combinações
apostas_por_ano = 365  # Apostando todo dia
anos_mega = combinacoes_mega / apostas_por_ano
anos_virada = combinacoes_total_virada / apostas_por_ano

print("⏰ Tempo para apostar TODAS as combinações (1 aposta por dia):")
print(f"   Mega-Sena: {anos_mega:,.0f} anos (≈ {anos_mega/1000:,.1f} milênios)")
print(f"   Mega Virada: {anos_virada:,.0f} anos (≈ {anos_virada/1000000:,.1f} milhões de anos)")

print(f"\n🌌 Contexto cósmico:")
print(f"   • Idade do Universo: ≈ 13.8 bilhões de anos")
print(f"   • Mega-Sena: {anos_mega/13800000000:.3f}× a idade do universo")
print(f"   • Mega Virada: {anos_virada/13800000000:.1f}× a idade do universo")

# 7. CONCLUSÃO
# ===============================================
print("\n" + "=" * 70)
print("🎯 CONCLUSÃO")
print("=" * 70)

print("📊 RESULTADOS DA SIMULAÇÃO:")
print(f"   Mega-Sena: {acertos_mega} acertos em {n_simulacoes:,} tentativas")
print(f"   Mega Virada: {acertos_virada} acertos em {n_simulacoes:,} tentativas")

print(f"\n✅ A Mega-Sena é significativamente mais provável!")
print(f"   Fator: {razao:,.0f} vezes mais chances de ganhar")
print(f"\n💡 LEMBRETE: Ambas as probabilidades são EXTREMAMENTE BAIXAS!")
print("   Jogue com responsabilidade! 🎲")