import math
import numpy as np
import matplotlib.pyplot as plt

def equacao_quadratica(a, b, c):
    # Calcula o discriminante (delta)
    delta = b**2 - 4*a*c
    print(f"Delta = {delta}")

    # Calcula as raízes
    if delta < 0:
        print("Não existem raízes reais")
        raizes = []
    elif delta == 0:
        x = -b / (2*a)
        print(f"Raiz única: x = {x}")
        raizes = [x]
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Duas raízes reais: x1 = {x1}, x2 = {x2}")
        raizes = [x1, x2]

    # Criar gráfico da função quadrática
    x = np.linspace(-10, 10, 400)  # gera pontos no eixo x
    y = a*x**2 + b*x + c           # equação quadrática

    plt.figure(figsize=(8,6))
    plt.plot(x, y, label=f'{a}x² + {b}x + {c}', color="blue")

    # Marcar raízes no gráfico (se existirem)
    for r in raizes:
        plt.plot(r, 0, 'ro', label=f"Raiz: {r:.2f}")

    plt.axhline(0, color="black", linewidth=1)  # eixo x
    plt.axvline(0, color="black", linewidth=1)  # eixo y
    plt.title("Função Quadrática")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show(block=False)

# === Exemplo de chamada ===
equacao_quadratica(1, -3, 2)  # f(x) = x² - 3x + 2
equacao_quadratica(1, -2, 1)  # f(x) = x² - 2x + 1
equacao_quadratica(1, 2, 5)   # f(x) = x² + 2x + 5
equacao_quadratica(10, 2, -52)   
equacao_quadratica(-10, -2, 52)   

# print(equacao_quadratica(1, -3, 2))   # Equação: x² - 3x + 2 = 0
# print(equacao_quadratica(1, -2, 1))   # Equação: x² - 2x + 1 = 0
# print(equacao_quadratica(1, 2, 5))    # Equação: x² + 2x + 5 = 0

input("Pressione Enter para fechar os gráficos...")
plt.close('all')