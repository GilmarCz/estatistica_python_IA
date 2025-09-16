import random

baralho = ['A_copas','2_copas','3_copas','4_copas','5_copas','6_copas','7_copas','8_copas','9_copas','10_copas','J_copas','Q_copas','K_copas'] + \
          ['A_ouros','2_ouros','3_ouros','4_ouros','5_ouros','6_ouros','7_ouros','8_ouros','9_ouros','10_ouros','J_ouros','Q_ouros','K_ouros'] + \
          ['A_paus','2_paus','3_paus','4_paus','5_paus','6_paus','7_paus','8_paus','9_paus','10_paus','J_paus','Q_paus','K_paus'] + \
          ['A_espadas','2_espadas','3_espadas','4_espadas','5_espadas','6_espadas','7_espadas','8_espadas','9_espadas','10_espadas','J_espadas','Q_espadas','K_espadas']

simulacoes = [random.choice(baralho) for _ in range(10000)]

# Agora filtrando só 3, 4 ou 5 de copas
cartas_copas_345 = [
    carta for carta in simulacoes
    if carta in ("3_copas", "4_copas", "5_copas")
]

prob = len(cartas_copas_345) / len(simulacoes)
print("A probabilidade é:", prob)