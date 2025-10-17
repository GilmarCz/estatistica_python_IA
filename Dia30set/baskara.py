import math

# Função para resolver ax^2 + bx + c = 0
def bhaskara(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Não possui raízes reais"
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    return x1, x2

# Exemplo de uso
raizes = bhaskara(1, -3, 2)
print("Raízes da equação:", raizes)
