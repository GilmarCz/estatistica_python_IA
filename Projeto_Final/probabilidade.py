import random
# 1) Urna com bolas coloridas
# Uma urna contém 5 bolas vermelhas e 7 azuis.
# Qual a probabilidade de retirar uma bola vermelha?
# calcular a probabilidade de sair 2 vermelhas na sequência (com e sem reposição)

vermelhas = 5
azuis = 7
total = vermelhas + azuis

# i) Probabilidade de uma vermelha
p_vermelha = vermelhas / total
print(f"Probabilidade de tirar 1 vermelha: {p_vermelha:.4f} ({p_vermelha*100:.2f}%)")

#i) Probabilidade de tirar 1 vermelha: 0.4167 (41.67%)

# ii) Duas vermelhas COM reposição
p_duas_com_reposicao = (vermelhas / total) * (vermelhas / total)
print(f"Duas vermelhas (com reposição): {p_duas_com_reposicao:.4f} ({p_duas_com_reposicao*100:.2f}%)")

#ii) Duas vermelhas (com reposição): 0.1736 (17.36%)

# iii) Duas vermelhas SEM reposição
p_duas_sem_reposicao = (vermelhas / total) * ((vermelhas - 1) / (total - 1))
print(f"Duas vermelhas (sem reposição): {p_duas_sem_reposicao:.4f} ({p_duas_sem_reposicao*100:.2f}%)")

#iii) Duas vermelhas (sem reposição): 0.1515 (15.15%)

# 2) Lançamento de um dado
# Qual a probabilidade de sair um número maior que 3 ao lançar um dado de 6 lados?

lados = [1, 2, 3, 4, 5, 6]
favoraveis = [x for x in lados if x > 3]

p_maior_que_3 = len(favoraveis) / len(lados)
print(f"2) Probabilidade de sair número > 3 = {p_maior_que_3:.4f} ({p_maior_que_3*100:.2f}%)")

#2) Probabilidade de sair número > 3 = 0.5000 (50.00%)

# 3) Lançamento de duas moedas
# Qual a probabilidade de sair exatamente uma cara ao lançar duas moedas?

# Espaço amostral:
# C = Cara, X = Coroa
# S = {CC, CX, XC, XX}

espaco = ['CC', 'CX', 'XC', 'XX']

# Contar os eventos com exatamente uma cara
favoraveis = [e for e in espaco if e.count('C') == 1]
p_uma_cara = len(favoraveis) / len(espaco)

print(f"3) Probabilidade de sair exatamente uma cara = {p_uma_cara:.4f} ({p_uma_cara*100:.2f}%)")

#3) Probabilidade de sair exatamente uma cara = 0.5000 (50.00%)

# 4) Probabilidade condicional (sem reposição)
# Uma urna tem 3 bolas vermelhas e 2 verdes.
# Se uma bola é retirada sem reposição e sai vermelha,
# qual a probabilidade da próxima ser verde?

vermelhas = 3
verdes = 2

# Após retirar uma vermelha → sobram 2 vermelhas e 2 verdes (total = 4)
restantes = (vermelhas - 1) + verdes
p_verde_dps_vermelha = verdes / restantes

print(f"4) Probabilidade da próxima ser verde (dada vermelha antes) = {p_verde_dps_vermelha:.4f} ({p_verde_dps_vermelha*100:.2f}%)")

#4) Probabilidade da próxima ser verde (dada vermelha antes) = 0.5000 (50.00%)


print("\nCálculos concluídos com sucesso!")
