import numpy as np
import matplotlib.pyplot as plt

# Configuração inicial
np.random.seed(42)
n_experimentos = 1_000_000
λ = 2  # Valor de λ para E(x) = 1/λ
valor_esperado = 1 / λ  # Valor teórico esperado = 0.5

# Simulando variáveis aleatórias exponenciais com parâmetro lambda = λ
# A distribuição exponencial tem E[X] = 1/lambda = 1/λ
lancamentos = np.random.exponential(scale=valor_esperado, size=n_experimentos)

# Calculando a média acumulada (Lei dos Grandes Números)
somas_acumuladas = np.cumsum(lancamentos) 
indices = np.arange(1, n_experimentos + 1) 
medias_acumuladas = somas_acumuladas / indices

# Criando o gráfico
plt.figure(figsize=(10, 5))
plt.plot(medias_acumuladas, label="Média amostral acumulada", color='green', alpha=0.8)
plt.axhline(valor_esperado, color="gold", linestyle="--", linewidth=2, 
           label=f"Valor esperado teórico E(X) = 1/{λ} = {valor_esperado}")

plt.xlabel("Número de observações", fontsize=12)
plt.ylabel("Média acumulada", fontsize=12)
plt.title("Lei dos Grandes Números: Convergência da Média Amostral para E(X) = 1/2", 
          fontsize=14, fontweight='bold')
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)

# Adicionando informações no gráfico
plt.text(n_experimentos*0.7, valor_esperado*1.1, 
         f'Valor final: {medias_acumuladas[-1]:.4f}', 
         bbox=dict(facecolor='white', alpha=0.8))

plt.tight_layout()
plt.show()

# Estatísticas finais
print(f"\nValor teórico esperado E(X): {valor_esperado:.4f}")
print(f"Valor da média amostral final: {medias_acumuladas[-1]:.4f}")
print(f"Diferença absoluta: {abs(medias_acumuladas[-1] - valor_esperado):.6f}")
print(f"Número de observações: {n_experimentos}\n")