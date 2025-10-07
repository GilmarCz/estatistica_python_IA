import cmath  # versão complexa da biblioteca math
import numpy as np
import matplotlib.pyplot as plt

def equacao_quadratica(a, b, c):
    # Calcula o discriminante
    delta = b**2 - 4*a*c
    print(f"Delta = {delta}")

    # Calcula raízes com cmath (funciona para delta < 0)
    x1 = (-b + cmath.sqrt(delta)) / (2*a)
    x2 = (-b - cmath.sqrt(delta)) / (2*a)

    print(f"Raízes: x1 = {x1}, x2 = {x2}")

    # Gerar gráfico da parábola
    x = np.linspace(-10, 10, 400)
    y = a*x**2 + b*x + c

    plt.figure(figsize=(8,6))
    plt.plot(x, y, label=f'{a}x² + {b}x + {c}', color="blue")

    # As raízes complexas não aparecem no eixo real, então não serão plotadas
    plt.axhline(0, color="black", linewidth=1)
    plt.axvline(0, color="black", linewidth=1)
    plt.title("Função Quadrática (Δ < 0 → raízes complexas)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()

# Exemplo: f(x) = x² + 2x + 5 → Δ = -16
equacao_quadratica(1, 2, 5)

equacao_quadratica(1, 0, -2)  # f(x) = x² - 2 (raízes ±√2 ≈ ±1.414)
