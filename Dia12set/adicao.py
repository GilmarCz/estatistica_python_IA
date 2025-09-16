def probabilidade_uniao(evento_A, evento_B, espaco_amostral):
    """
    Calcula P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
    
    Parâmetros:
        evento_A (set): conjunto de elementos do evento A
        evento_B (set): conjunto de elementos do evento B
        espaco_amostral (set): conjunto com todos os resultados possíveis
    
    Retorna:
        float: probabilidade de A ou B
    """
    total = len(espaco_amostral)
    
    prob_A = len(evento_A) / total
    prob_B = len(evento_B) / total
    intersecao = evento_A.intersection(evento_B)
    prob_intersec = len(intersecao) / total

    prob_union = prob_A + prob_B - prob_intersec
    return prob_union
    # Espaço amostral do dado
espaco_amostral = {1, 2, 3, 4, 5, 6}

# Evento A: número par
A = {2, 4, 6}

# Evento B: número > 4
B = {5, 6}

# Cálculo da probabilidade
p = probabilidade_uniao(A, B, espaco_amostral)
print(f"Probabilidade de A ou B: {p:.2f} ou {p*100:.0f}%")