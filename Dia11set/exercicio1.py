import numpy as np
import matplotlib.pyplot as plt

# Reprodutibilidade
np.random.seed(42)

# Parâmetros
λ = 2                    # taxa (lambda)
scale = 1.0 / λ          # parâmetro 'scale' do np.random.exponential = 1/lambda
N = 100_000              # número de amostras (aumente para ver convergência melhor)

# Gera N amostras da distribuição exponencial (média teórica = 1/λ)
amostras = np.random.exponential(scale=scale, size=N)

# Calcula a média acumulada: soma acumulada / (1, 2, ..., N)
somas_acumuladas = np.cumsum(amostras)               # soma acumulada das amostras
indices = np.arange(1, N + 1)                        # denominador para cada passo
medias_acumuladas = somas_acumuladas / indices       # média amostral após cada amostra

# Plot principal
plt.figure(figsize=(10, 5))
plt.plot(medias_acumuladas, label="Média amostral acumulada")
plt.axhline(1.0 / λ, linestyle="--", linewidth=2,
            label=f"Valor esperado teórico = 1/{λ} = {1.0/λ:.3f}")
plt.xlabel("Número de amostras")
plt.ylabel("Média acumulada")
plt.title("Lei dos Grandes Números — distribuição Exponencial (λ=2)")
plt.legend()
plt.grid(alpha=0.3)

# Opcional: mostrar uma janela inicial em detalhe (zoom) para ver as flutuações pequenas
# (aqui desenhamos um eixo secundário apenas para zoom visual)
ax = plt.gca()
ax.set_xlim(0, N)               # mostrar todo o intervalo
# Se quiser ver melhor o começo, descomente as duas linhas abaixo:
# plt.figure(figsize=(10,4))
# plt.plot(medias_acumuladas[:2000]); plt.axhline(1.0/y, linestyle='--')

plt.show()
