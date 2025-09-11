import random
from collections import Counter   # Útil para contar ocorrências de cada resultado
import matplotlib.pyplot as plt   # Biblioteca para gráficos

# Espaço amostral de dois lançamentos de moeda:
# ('C', 'C') = cara e cara
# ('C', 'K') = cara e coroa
# ('K', 'C') = coroa e cara
# ('K', 'K') = coroa e coroa
espaco_amostral = [("C", "C"), ("C", "K"), ("K", "C"), ("K", "K")]
#espaco_amostral = [(a,b) for a in ['C','K'] for b in ['C','K']]

# Número de experimentos (quantos pares de lançamentos vamos simular)
N = 10000

# Simulação: gera N pares de lançamentos
# random.choice(["C", "K"]) escolhe aleatoriamente entre "C" (cara) e "K" (coroa)
# cada par é um tupla (primeiro_lancamento, segundo_lancamento)
resultados = [
    (random.choice(["C", "K"]), random.choice(["C", "K"]))
    for _ in range(N)
]

# Conta quantas vezes cada resultado apareceu
# Exemplo: {('C','C'): 2512, ('C','K'): 2487, ...}
contagem = Counter(resultados)

# Calcula as frequências empíricas (proporções observadas)
# divide a contagem de cada evento por N (total de experimentos)
frequencias_empiricas = {evento: contagem[evento]/N for evento in espaco_amostral}

# Frequências teóricas: como a moeda é justa, cada evento tem probabilidade 1/4 = 0.25
frequencias_teoricas = {evento: 0.25 for evento in espaco_amostral}

# Exibe os resultados
print("Frequências teóricas:")
for evento, p in frequencias_teoricas.items():
    print(f"{evento}: {p:.4f}")    # :.4f -> formata número com 4 casas decimais

print("\nFrequências empíricas (simulação):")
for evento, p in frequencias_empiricas.items():
    print(f"{evento}: {p:.4f}")

# --- Gráfico de barras ---
eventos = [str(e) for e in espaco_amostral]           # Converte tuplas para string p/ rótulos
valores_teoricos = [frequencias_teoricas[e] for e in espaco_amostral]
valores_empiricos = [frequencias_empiricas[e] for e in espaco_amostral]

largura = 0.35   # Largura das barras

plt.figure(figsize=(8,5))
# Barras teóricas (deslocadas um pouco à esquerda)
plt.bar(
    [i - largura/2 for i in range(len(eventos))],
    valores_teoricos,
    width=largura,
    label="Teórica (0.25 cada)"
)
# Barras empíricas (deslocadas à direita)
plt.bar(
    [i + largura/2 for i in range(len(eventos))],
    valores_empiricos,
    width=largura,
    label="Empírica (simulação)"
)

plt.xticks(range(len(eventos)), eventos)   # Rótulos no eixo X
plt.ylabel("Frequência")
plt.title("Dois lançamentos de moeda — Frequências teóricas vs empíricas")
plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.show()