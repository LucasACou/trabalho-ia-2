import utils.genetica as gen
import random as rand
import copy

padrao = [2,2,1,3,3,2,1,2,4]
numero_individuo = 100
aluno_real = []
for _ in range(8):
    linha = [
        max(0, min(4, gene + rand.randint(-1,1)))
        for gene in padrao
    ]
    aluno_real.append(linha)
populacao = gen.newpop(numero_individuo)
loop = 0


#LOOP REAL
while loop != 8:
    #ações do aluno real
    acoes = aluno_real[loop]

    for individuo in populacao:
        individuo[1] = [1] * 9

#--------------------------------------------------------(EVALUATION)
    for  i in range(numero_individuo):

        #calcula o score do cromossomo
        score = gen.avaliar_genes(populacao[i], acoes)

        #atualiza o peso do cromossomo
        gen.atualizar_peso(populacao[i], score)

    elite = copy.deepcopy(max(populacao, key=lambda ind: gen.fitness(ind)))
    nova_pop = [elite]

#---------------------------------------------------------(SELECTION)
    while len(nova_pop) < numero_individuo:

        #seleciona melhores cromossomos para serem pais
        #pai1 = gen.selecao(populacao)
        #pai2 = gen.selecao(populacao)
        pai1 = gen.selecao_torneio(populacao)
        pai2 = gen.selecao_torneio(populacao)

        while pai1 == pai2:
            #pai2 = gen.selecao(populacao)
            pai2 = gen.selecao_torneio(populacao)

#---------------------------------------------------------(CROSSOVER)
        filho1, filho2 = gen.crossover(pai1, pai2)

        nova_pop.append(filho1)
        if len(nova_pop) < numero_individuo:
            nova_pop.append(filho2)

    populacao = nova_pop

#-----------------------------------------------------------(MUTAÇÂO)
    for i in range(numero_individuo):
        gen.mutacao(populacao[i], False)

    loop += 1

for i in range(numero_individuo):
    print(f"Cromossomo Final[{i + 1}]:")
    for sublista in populacao[i]:
        print(sublista)

melhor = max(populacao, key=lambda ind: gen.fitness(ind))
print(f"\nGENES DO MELHOR CROMOSSOMO:")
print(melhor[0])

processing, perception, understanding = gen.interpretar_estilo(melhor)

print("\nESTILO DE APRENDIZAGEM:")
print(f"Processing: {processing}")
print(f"Perception: {perception}")
print(f"Understanding: {understanding}")

acc = gen.calcular_accuracy(melhor, aluno_real)

print("\nACCURACY:")
print(f"Accuracy: {acc:.2f} ({acc*100:.2f}%)")

print("\nALUNO REAL:")
for i in range(8):
    print(aluno_real[i])






# #TESTE DE FUNÇÔES
# for i in range(numero_individuo):

#     #(INITIAL POPULATION)--------------------------------------------|
#     print(f"\nCromossomo[{i + 1}]:")

#     for sublista in populacao[i]:
#         print(sublista)

#     #ações do aluno real
#     print(f"\nAções[{i + 1}]:")
#     print(acoes)

#     #(EVALUATION)----------------------------------------------------|
#     print(f"\nScore[{i + 1}]:")
#     score = gen.avaliar_genes(populacao[i], acoes)
#     print(score)

#     #atualiza o peso do cromossomo
#     print(f"\nCromossomo com novo peso[{i + 1}]:")
#     gen.atualizar_peso(populacao[i], score)
#     for sublista in populacao[i]:
#         print(sublista)

#     #calcula o fitness do cromossomo
#     fitness = gen.fitness(populacao[i])
#     print(f"\nFitness[{i + 1}]:{fitness}")

# nova_pop = []

# for i in range(numero_individuo//2):
#     #(SELECTION)-----------------------------------------------------|
#     #seleciona melhores cromossomos para serem pais
#     pai1 = gen.selecao(populacao)
#     pai2 = gen.selecao(populacao)

#     print("\nCromossomo pai:")
#     print(pai1[0])
#     print(pai1[1])
#     print("\nCromossomo pai:")
#     print(pai2[0])
#     print(pai2[1])

#     while pai1 == pai2:
#         pai2 = gen.selecao(populacao)

#     #(CROSSOVER)-----------------------------------------------------|
#     filho1, filho2 = gen.crossover(pai1, pai2)

#     nova_pop.append(filho1)
#     nova_pop.append(filho2)

# populacao = nova_pop
# #print("\n", populacao)

# for i in range(numero_individuo):

#     print(f"\nCromossomo filho[{i + 1}]:")
#     for sublista in nova_pop[i]:
#         print(sublista)


# for i in range(numero_individuo):
    
#     #(MUTAÇÂO)-------------------------------------------------------|
#     gen.mutacao(populacao[i])
#     print(f"Cromossomo filho[{i + 1}]:")
#     for sublista in nova_pop[i]:
#         print(sublista)
