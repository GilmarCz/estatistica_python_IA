# equação quadrática ax^2+bx+c=0
# baskara = -b +-(raiz de delta)/2a  delta = (b^2 -4ac)

import math

def baskara(a, b, c):
    # Calcula o discriminante (delta)
    delta = b**2 - 4*a*c
    print(f"Delta = {delta}")

    if delta < 0:
        return "Não existem raízes reais"
    elif delta == 0:
        x = -b / (2*a)
        return f"Raiz única: x = {x}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"Duas raízes reais: x1 = {x1}, x2 = {x2}"

# Exemplo de uso:
print(baskara(1, -3, 2))   # Equação: x² - 3x + 2 = 0
print(baskara(1, -2, 1))   # Equação: x² - 2x + 1 = 0
print(baskara(1, 2, 5))    # Equação: x² + 2x + 5 = 0
