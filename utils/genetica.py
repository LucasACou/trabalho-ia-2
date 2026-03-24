import random as rand

N_CODE = 9
N_WEIGHT = 2
M_TAX = 0.01

def newpop(numero_individuo):
    """
    Gera nova população.

    """

    nova_populacao = []
    
    for _ in range(numero_individuo):
        individuo = [[0 for _ in range(N_CODE)] for _ in range(N_WEIGHT)]

        for j in range(N_CODE):
            individuo[0][j] = rand.randint(0, 4)
            individuo[1][j] = rand.randint(1, 3)

        nova_populacao.append(individuo)

    return nova_populacao

def avaliar_genes(individuo, acoes):

    code = individuo[0]
    score = [0] * len(code)

    for i in range(len(code)):
        if code[i] == acoes[i]:
            score[i] = 1
        
    return score

def atualizar_peso(individuo, score):
    weight = individuo[1]
    new_weight = [0] * len(weight)

    for i in range(len(weight)):
        new_weight[i] = weight[i] + score[i]

    individuo[1] = new_weight

    return

def fitness(individuo):
    weight = individuo[1]
    return sum(weight)

def selecao(populacao):

    fitnesses = [fitness(individuo) for individuo in populacao]

    if sum(fitnesses) == 0:
        return rand.choice(populacao)
    
    soma_fitness = sum(fitnesses)
    probabilidades = [f / soma_fitness for f in fitnesses]

    escolhidos = rand.choices(populacao, weights=probabilidades, k=1)

    return escolhidos[0]


def crossover(pai1, pai2):

    filho1 = [[], []]
    filho2 = [[], []]

    #code
    filho1[0] = pai1[0][:3] + pai2[0][3:7] + pai1[0][7:]
    filho2[0] = pai2[0][:3] + pai1[0][3:7] + pai2[0][7:]

    #weight
    filho1[1] = pai1[1][:3] + pai2[1][3:7] + pai1[1][7:]
    filho2[1] = pai2[1][:3] + pai1[1][3:7] + pai2[1][7:]

    return filho1, filho2

def mutacao(individuo, occur=True):
    if rand.random() < M_TAX:
        if occur == True:
            print("\nOcorreu mutação!")
        code = individuo[0]
        gene_escolhido = rand.randint(0,8)
        temp = rand.randint(0,4)

        while temp == code[gene_escolhido]:
            temp = rand.randint(0,4)

        code[gene_escolhido] = temp
        individuo[0] = code

def interpretar_estilo(individuo):
    code = individuo[0]

    S1 = code[0] + code[1]

    #PROCESSING
    if S1 == 0:
        processing = "Extremely passive"
    elif S1 == 1:
        processing = "Medium passive"
    elif S1 in [2,3]:
        processing = "Neutral"
    elif S1 == 4:
        processing = "Medium active"
    else:
        processing = "Extremely active"

    S2 = sum(code[2:8])

    #PERCEPTION
    if S2 <= 4:
        perception = "Extremely intuitive"
    elif S2 <= 8:
        perception = "Medium intuitive"
    elif S2 <= 16:
        perception = "Neutral"
    elif S2 <= 20:
        perception = "Medium sensitive"
    else:
        perception = "Extremely sensitive"

    # UNDERSTANDING
    g9 = code[8]
    mapa = {
        0: "Extremely sequential",
        1: "Medium sequential",
        2: "Neutral",
        3: "Medium global",
        4: "Extremely global"
    }
    understanding = mapa[g9]

    return processing, perception, understanding

def calcular_accuracy(melhor, aluno_real):
    genes = melhor[0]
    total_acoes = 0
    acertos = 0

    for unidade in aluno_real:
        for i in range(9):
            total_acoes += 1
            if abs(genes[i] - unidade[i]) <= 1:
                acertos += 1

    return acertos / total_acoes