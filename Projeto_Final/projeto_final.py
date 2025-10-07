import os

# ==============================
# Funções auxiliares
# ==============================

def abrir_pdf(nome_arquivo):
    """Abre um arquivo PDF no visualizador padrão (Windows)."""
    if not os.path.exists(nome_arquivo):
        print("Arquivo não encontrado! Verifique o caminho ou mova o PDF para a pasta do programa.")
        return
    try:
        os.startfile(nome_arquivo)
        print(f"\nAbrindo {nome_arquivo}...\n")
    except Exception as e:
        print(f"Erro ao abrir o arquivo: {e}")

# ==============================
# QUIZ 1 — Estatística em IA
# ==============================

def quiz_estatistica():
    perguntas = [
        {
            "pergunta": "1️ Qual é a distribuição mais usada para modelar erros em regressão linear?",
            "opcoes": ["a) Uniforme", "b) Normal", "c) Exponencial", "d) Binomial"],
            "resposta": "b"
        },
        {
            "pergunta": "2️ O que é variância?",
            "opcoes": [
                "a) Medida de tendência central.",
                "b) Medida de dispersão dos dados em relação à média.",
                "c) Valor máximo do conjunto.",
                "d) Diferença entre o maior e o menor valor."
            ],
            "resposta": "b"
        },
        {
            "pergunta": "3️ Em uma distribuição normal, cerca de 68% dos dados estão:",
            "opcoes": [
                "a) Dentro de 1 desvio padrão da média",
                "b) Dentro de 2 desvios padrão da média",
                "c) Dentro de 3 desvios padrão da média",
                "d) Fora da média"
            ],
            "resposta": "a"
        },
        {
            "pergunta": "4️ A média é afetada fortemente por:",
            "opcoes": ["a) Outliers", "b) Moda", "c) Mediana", "d) Tamanho da amostra"],
            "resposta": "a"
        },
        {
            "pergunta": "5️ O histograma serve para:",
            "opcoes": [
                "a) Mostrar a frequência de valores contínuos.",
                "b) Exibir relações entre duas variáveis.",
                "c) Apresentar valores categóricos.",
                "d) Calcular médias e medianas."
            ],
            "resposta": "a"
        },
        {
            "pergunta": "6️ O desvio padrão mede:",
            "opcoes": [
                "a) O quanto os dados variam em torno da média.",
                "b) A quantidade de dados.",
                "c) A soma dos valores.",
                "d) O ponto máximo da distribuição."
            ],
            "resposta": "a"
        },
        {
            "pergunta": "7️ A moda é:",
            "opcoes": [
                "a) O valor mais frequente no conjunto de dados.",
                "b) O valor médio.",
                "c) A diferença entre extremos.",
                "d) A soma de todos os valores."
            ],
            "resposta": "a"
        },
        {
            "pergunta": "8️ Qual das opções representa uma variável qualitativa?",
            "opcoes": [
                "a) Altura",
                "b) Peso",
                "c) Cor dos olhos",
                "d) Idade"
            ],
            "resposta": "c"
        },
        {
            "pergunta": "9️ Qual é a fórmula da probabilidade clássica?",
            "opcoes": [
                "a) Casos favoráveis / Casos possíveis",
                "b) Casos possíveis / Casos favoráveis",
                "c) (A + B) / 2",
                "d) n! / k!"
            ],
            "resposta": "a"
        },
        {
            "pergunta": "10 Em um gráfico de dispersão, o que representa a tendência dos pontos?",
            "opcoes": [
                "a) Correlação",
                "b) Moda",
                "c) Frequência",
                "d) Variância"
            ],
            "resposta": "a"
        },
    ]

    acertos = 0
    for q in perguntas:
        print("\n" + q["pergunta"])
        for op in q["opcoes"]:
            print(op)
        resp = input("Sua resposta: ").lower().strip()
        if resp == q["resposta"]:
            print("Correto!")
            acertos += 1
        else:
            print(f"Errado! Resposta correta: {q['resposta'].upper()}")

    print(f"\nResultado final: {acertos}/{len(perguntas)} acertos.\n")

# ==============================
# QUIZ 2 — Machine Learning
# ==============================

def quiz_ml():
    perguntas = [
        {
            "pergunta": "1️ O que é overfitting?",
            "opcoes": [
                "a) Modelo que generaliza bem.",
                "b) Modelo que memoriza dados de treino e erra em novos dados.",
                "c) Modelo simples demais.",
                "d) Modelo com poucos parâmetros."
            ],
            "resposta": "b"
        },
        {
            "pergunta": "2️ O que é underfitting?",
            "opcoes": [
                "a) Quando o modelo aprende demais.",
                "b) Quando o modelo não aprende o suficiente e tem baixa precisão.",
                "c) Quando há muitos dados de treino.",
                "d) Quando o modelo é regularizado."
            ],
            "resposta": "b"
        },
        {
            "pergunta": "3️ Qual é o objetivo da regularização?",
            "opcoes": [
                "a) Aumentar o erro de treino.",
                "b) Diminuir pesos grandes e evitar overfitting.",
                "c) Tornar o modelo mais complexo.",
                "d) Melhorar a velocidade de treino."
            ],
            "resposta": "b"
        },
        {
            "pergunta": "4️ O que é uma função de custo?",
            "opcoes": [
                "a) Mede o erro entre previsão e valor real.",
                "b) Mede a precisão do modelo.",
                "c) Mede o tempo de execução.",
                "d) Mede o tamanho do dataset."
            ],
            "resposta": "a"
        },
        {
            "pergunta": "5️ Qual é o algoritmo mais usado para regressão linear?",
            "opcoes": [
                "a) Gradient Descent",
                "b) K-Means",
                "c) Naive Bayes",
                "d) Decision Tree"
            ],
            "resposta": "a"
        },
        {
            "pergunta": "6️ Qual é a principal métrica usada em classificação binária?",
            "opcoes": ["a) Acurácia", "b) RMSE", "c) MSE", "d) R²"],
            "resposta": "a"
        },
        {
            "pergunta": "7️ O que é um dataset de treino?",
            "opcoes": [
                "a) Dados usados para avaliar o modelo.",
                "b) Dados usados para ajustar os parâmetros do modelo.",
                "c) Dados sem rótulo.",
                "d) Dados descartados."
            ],
            "resposta": "b"
        },
        {
            "pergunta": "8️ Qual biblioteca Python é mais usada para machine learning tradicional?",
            "opcoes": ["a) TensorFlow", "b) PyTorch", "c) Scikit-learn", "d) Numpy"],
            "resposta": "c"
        },
        {
            "pergunta": "9️ O que é uma rede neural?",
            "opcoes": [
                "a) Um conjunto de algoritmos que simulam o cérebro humano.",
                "b) Um modelo baseado em árvores de decisão.",
                "c) Um método de regressão linear.",
                "d) Um sistema de estatísticas simples."
            ],
            "resposta": "a"
        },
        {
            "pergunta": "10 O que é uma feature em machine learning?",
            "opcoes": [
                "a) A variável de saída.",
                "b) Um dado irrelevante.",
                "c) Uma característica (entrada) usada pelo modelo.",
                "d) Um tipo de erro."
            ],
            "resposta": "c"
        },
    ]

    acertos = 0
    for q in perguntas:
        print("\n" + q["pergunta"])
        for op in q["opcoes"]:
            print(op)
        resp = input("Sua resposta: ").lower().strip()
        if resp == q["resposta"]:
            print("Correto!")
            acertos += 1
        else:
            print(f"Errado! Resposta correta: {q['resposta'].upper()}")

    print(f"\nResultado final: {acertos}/{len(perguntas)} acertos.\n")

# ==============================
# MENU PRINCIPAL
# ==============================

def menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Exercícios resolvidos de Estatística (PDF)")
        print("2 - Quiz: Estatística em IA")
        print("3 - Quiz: Machine Learning")
        print("4 - Pesquisa sobre uso de IA (PDF)")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            abrir_pdf(r"C:\Users\gilmar.2970\Desktop\UC4_Estatistica\Dia25set\Relatorio_Voos_Com_exercicio_extra.pdf")
        elif opcao == "2":
            quiz_estatistica()
        elif opcao == "3":
            quiz_ml()
        elif opcao == "4":
            abrir_pdf(r"C:\Users\gilmar.2970\Desktop\UC4_Estatistica\Projeto_Final\pesquisa_ia.pdf")
        elif opcao == "0":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# ==============================
# EXECUÇÃO PRINCIPAL
# ==============================
if __name__ == "__main__":
    menu()
