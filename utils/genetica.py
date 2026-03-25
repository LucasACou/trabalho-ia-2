import random as rand

N_CODE = 9
N_WEIGHT = 2
M_TAX = 0.01

def newpop(numero_individuo):
    """
    Gera uma nova população de indivíduos.

    Cada indivíduo é composto por:
    - Uma lista de códigos (genes)
    - Uma lista de pesos

    Args:
        numero_individuo (int): quantidade de indivíduos na população

    Returns:
        list: lista de indivíduos gerados
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
    """
    Avalia os genes de um indivíduo comparando com ações esperadas.

    Args:
        individuo (list): indivíduo contendo código e pesos
        acoes (list): lista de ações esperadas

    Returns:
        list: lista de pontuação (1 para acerto, 0 para erro)
    """
    code = individuo[0]
    score = [0] * len(code)

    for i in range(len(code)):
        if code[i] == acoes[i]:
            score[i] = 1
        
    return score

def atualizar_peso(individuo, score):
    """
    Atualiza os pesos de um indivíduo com base na pontuação obtida.

    Args:
        individuo (list): indivíduo a ser atualizado
        score (list): lista de pontuação obtida

    Returns:
        None
    """
    weight = individuo[1]
    new_weight = [0] * len(weight)

    for i in range(len(weight)):
        new_weight[i] = weight[i] + score[i]

    individuo[1] = new_weight

    return

def fitness(individuo):
    """
    Calcula o fitness de um indivíduo.

    O fitness é definido como a soma dos pesos.

    Args:
        individuo (list): indivíduo avaliado

    Returns:
        int: valor do fitness
    """
    weight = individuo[1]
    return sum(weight)

def selecao(populacao):
    """
    Seleção por roleta (fitness proporcional).

    Indivíduos com maior fitness têm maior probabilidade de serem escolhidos.

    Args:
        populacao (list): lista de indivíduos

    Returns:
        list: indivíduo selecionado
    """
    fitnesses = [fitness(individuo) for individuo in populacao]

    if sum(fitnesses) == 0:
        return rand.choice(populacao)
    
    soma_fitness = sum(fitnesses)
    probabilidades = [f / soma_fitness for f in fitnesses]

    escolhidos = rand.choices(populacao, weights=probabilidades, k=1)

    return escolhidos[0]

def selecao_torneio(populacao, k=3):
    """
    Seleção por torneio.

    Seleciona k indivíduos aleatórios e retorna o melhor entre eles.

    Args:
        populacao (list): lista de indivíduos
        k (int): tamanho do torneio

    Returns:
        list: indivíduo selecionado
    """
    # escolhe k indivíduos aleatórios da população
    torneio = rand.sample(populacao, k)

    # retorna o indivíduo com maior fitness
    melhor = max(torneio, key=lambda individuo: fitness(individuo))

    return melhor

def crossover(pai1, pai2):
    """
    Realiza o cruzamento entre dois pais gerando dois filhos.

    O cruzamento é feito por segmentos fixos dos genes.

    Args:
        pai1 (list): primeiro indivíduo
        pai2 (list): segundo indivíduo

    Returns:
        tuple: dois indivíduos filhos (filho1, filho2)
    """
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
    """
    Aplica mutação em um indivíduo com probabilidade M_TAX=0.01.

    A mutação altera aleatoriamente um gene do código.

    Args:
        individuo (list): indivíduo a ser mutado
        occur (bool): indica se deve imprimir mensagem de mutação

    Returns:
        None
    """
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
    """
    Interpreta o estilo de um indivíduo com base em seus genes.

    Classifica o indivíduo em três dimensões:
    - Processing
    - Perception
    - Understanding

    Args:
        individuo (list): indivíduo a ser interpretado

    Returns:
        tuple: (processing, perception, understanding)
    """
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
    """
    Calcula a acurácia de um indivíduo em relação a dados reais.

    Considera acerto quando a diferença entre gene e valor real é <= 1.

    Args:
        melhor (list): indivíduo avaliado
        aluno_real (list): lista de ações reais do aluno

    Returns:
        float: taxa de acerto (entre 0 e 1)
    """
    genes = melhor[0]
    total_acoes = 0
    acertos = 0

    for unidade in aluno_real:
        for i in range(9):
            total_acoes += 1
            if abs(genes[i] - unidade[i]) <= 1:
                acertos += 1

    return acertos / total_acoes
