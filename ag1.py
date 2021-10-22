import math
import random

capacidade = 5.0
pesos = [0.20, 0.75, 0.55, 0.30, 0.80, 
        0.15, 0.45, 0.50, 0.70, 0.60,
        0.40, 0.80, 0.25, 0.35, 0.30,
        0.65, 0.20, 0.70, 0.55, 0.45]
### FUNCTION ---CRIAR CROMOSSOMO ALEATORIO---
# gera um cromossomo aleatorio. É utilizado
# durante a geracao da populacao inicial no 
# começo do algoritmo, antes dos operadores 
# geneticos (seleção, cruzamento e mutação)    
###
def criar_cromossomo_aleatorio(tamanho):
    cromossomo = list()
    for i in range(tamanho):
        gene = random.randint(0, 1)

        cromossomo.append(gene)
    
    return cromossomo
### FUNCTION ---CRIAR POPULACAO INICIAL---
# gera um numero de cromossomos aleatorios 
# para compor a populacao inicial baseado
# no tamanho dado pelo usuario  
###
def criar_populacao_inicial(tamanho_populacional, tamanho_cromossomo):
    populacao = list()
    for i in range(tamanho_populacional):
        cromossomo = criar_cromossomo_aleatorio(tamanho_cromossomo)

        populacao.append(cromossomo)

    return populacao
### FUNCTION ---MOSTRAR POPULACAO E APTIDAO---
# funcao para imprimir todos os individuos e 
# seus respectivos graus de aptidao de acordo
# com a funcao de aptidao estabelecida la em cima
### 
### FUNCTION ---FUNCAO SOMA DE PESOS--
# Função responsável por calcular a soma dos pesos 
# do livro do cromossomo escolhido para ser calculado
###
def soma_de_pesos(cromossomo):
    soma = 0 # soma do peso dos livros
    
    i = 0 # contador
    # verifica cada gene do cromossomo
    for gene in cromossomo:
        # se o gene for positivo então o 
        # livro está presente e deve ser 
        # incluido na soma dos livros
        if(gene == 1): 
            soma += pesos[i]
            # ----------DEBUG--------------
            #print(f'livro {i} existente')
            #print(f'peso do livro: {pesos[i]}kg')
            #print(f'pesagem atual:{soma:0.3f}kg')
            # -----------------------------
        i += 1 # incremento do contador

    return soma
### FUNCTION ---FUNÇÃO DE APTIDAO---
# Função que define o nivel de aptidão do cromossomo
# usando como função o numero de livros existentes na
# mochila. Para isso basta somarmos todos os genes uma 
# vez que os alelos existente são 1 e 0 os livros que 
# não estiverem presentes na mochila não contaram na
# soma.
###
def funcao_de_aptidao(cromossomo):
    soma = soma_de_pesos(cromossomo)

    # verifica a função de aptidao 
    aptidao = 0 # aptidao inicial
    if(soma > capacidade):
        # se o peso for maior que a mochila
        # puder carregar, a mochila rasga e 
        # portanto a aptidao desse cromossomo 
        # é zero (pior resultado possivel)
        return aptidao 
    else:
        # se o peso for dentro capacidade
        # ou igual a mesma, então devemos
        # calcular a quantidade de livros
        # presentes na mochila, ou seja
        # o numero de alelos positivos
        for gene in cromossomo:
            aptidao += gene * 10
            #----------DEBUG-------------
            #print(f'gene: {gene}')
            #print(f'aptidao: {aptidao}')
            #----------------------------
        # apenas para fins de ilustração
        # coloquei cada gene valendo 10 
        # a fim de que o resultado fique 
        # mais facil de se ler

    return aptidao # por ultimo retorna a aptidao
def porcentagem_da_aptidao(populacao):
    # Aqui nos vamos juntar todas as aptidões em uma
    # unica lista a fim de fazer a soma toda e tirar 
    # a porcentagem de aptidão de cada cromossomo em
    # comparação com os outros.
    aptidao_pop = list()
    for cromossomo in populacao:
        #---------------------------------------------
        #print(f'Cromossomo[{i}]: {cromossomo}') #DEBUG
        #---------------------------------------------
        # recebe a aptidao do cromossomo atual
        aptidao = funcao_de_aptidao(cromossomo)
        #------------------------------------
        #print(f'aptidão = {aptidao}') #DEBUG
        #------------------------------------
        # adiciona a aptidao do cromossomo a 
        # na lista de aptidões. 
        aptidao_pop.append(aptidao)
        # Por estar na mesma ordem da população 
        # para descobrimos a qual cromossomo se 
        # refere basta encontrarmos o index na 
        # lista de aptidões e joga-lo na lista
        # de cromossomos (array da população)  
    # agora que temos um array com todas as aptidoes
    # vamos comparar as entradas com as somas para
    # podermos atribuir as porcentagens a cada uma
    # das entradas (baseado no index de cada valor)  
    return aptidao_pop
### FUNCTION ---FUNCAO METODO DA ROLETA---
# Esse é um método de amostragem estocástica onde 
# cada cromossomo tem a probalidade de ser escolhido
# para a seleção de acordo com o seu valor de aptidao 
###
def metodo_roleta(lista_de_aptidoes):
    aptidao_total = sum(lista_de_aptidoes)
    # existe uma chance rara, mas possível, da aptidao total
    # ser zero, ou seja todos os individuos da lista tem a 
    # aptidao igual a zero 
    aptidao_porcento = list()
    for aptidao in lista_de_aptidoes:
        porcentagem = aptidao*100/aptidao_total
        aptidao_porcento.append(porcentagem)
    # tendo as porcentagens em mãos, precisamos agora 
    # arredondar esse floats em inteiros, para que possamos
    # fazer uma tabela com os valores relacionados a cada
    # um dos individuos (tendo sua probabilidade diretamente
    # relacionada a seu porcentagem de aptidao sobre o todo)
    aptidao_inteiro = list()

    i = 0
    for aptidao in lista_de_aptidoes:
        inteiro = math.floor(aptidao_porcento[i])
        aptidao_inteiro.append(inteiro)
        i += 1

    tabela_de_sorteio = list()
    i = 0
    for aptidao in lista_de_aptidoes:
        tabela_fracionada = [i+1] * aptidao_inteiro[i]
        # criamos uma parte da tabela so com os numeros 
        # que iram representar o individuo i, essa tabela
        # tera o tamanho da sua porcentagem de aptidao em 
        # inteiros. Portanto quanto maior a aptidao maior 
        # a chance dele ser sorteado 
        tabela_de_sorteio += tabela_fracionada
        # assim, toda vez que uma tabela do individuo for
        # criada ela será somada a tabela final na qual
        # sortearemos o individuo a ser relacionado   
        i += 1
    # agora é provavel que a tabela esteja faltando alguns 
    # elementos até o numero 100. Isso acontece por que uma 
    # vez que arredondamos o valor da porcentagem os numeros
    # após a virgula se perderam e a soma deles acaba por não
    # resultar zero. Caso isso aconteça iremos preencher o 
    # espaços faltantes com o número 0 que representa nenhum 
    # dos individuos dentro da lista de aptidoes (e da população)   
    i = 0
    for i in range(100 + 1):
        if len(tabela_de_sorteio) < i:
            tabela_de_sorteio.append(0) 
    #DEBUG-------------------
    #print(aptidao_inteiro)
    #print(tabela_de_sorteio)
    #------------------------

    # agora que temos uma tabela com os valores definidos de 
    # acordo com a porcentagem de chance dos individuos serem
    # escolhidos podemos sortea-los
    resultado = 0 
    while(resultado == 0):
        # sendo a tabela um matriz com 100 entradas as entradas
        # variam de 0 até 99 por isso esses numeros escolhidos 
        escolhido = random.randint(0, 99)
        # leve em consideração que  os numeros usado para preencher 
        # a tabela são escolhidos de 1 - n (sendo n o numero que  
        # representa o ultimo individuo da tabela) e o 0 representa 
        # uma casa vazia (sujeita a repetição do sorteio)
        resultado = tabela_de_sorteio[escolhido]
    return resultado - 1 
    # resultado corrigido para o numero de cromossomos presentes 
    # na população de cromossomos. 
### FUNCTION ---FUNÇÃO DE CRUZAMENTO---
# Nessa função é que são escolhido os pais de um novo
# individuo para que seja gerado a população de filhos 
# que também podem sofrer a mutação necessária.
# Uma vez que cada casal de pais gera dois filhos, o 
# numero de repetições do laço que os gera deve ser um 
# inteiro divido por dois, para condizer com o numero 
# esperado pela taxa de cruzamento dado na função main
###
def cruzamento(populacao, lista_de_aptidoes, taxa_de_cruzamento, taxa_de_mutacao):
    
    populacao_filhos = list()
    numero_de_filhos = math.floor(len(populacao) * taxa_de_cruzamento)
    
    ponto_de_cruzamento = 10 # meio exato do cromossomo
    total_de_genes = len(encontra_cromossomo(populacao,1))

    i = 0
    for i in range(numero_de_filhos//2):        
        # SELEÇÃO
        pai = metodo_roleta(lista_de_aptidoes)
        cromossomo_pai = encontra_cromossomo(populacao, pai)

        mae = metodo_roleta(lista_de_aptidoes)
        cromossomo_mae = encontra_cromossomo(populacao, mae)

        # verifica se o cromossomo mãe e o cromossomo pai são diferentes
        while cromossomo_pai == cromossomo_mae:
            mae = metodo_roleta(lista_de_aptidoes)
            cromossomo_mae = encontra_cromossomo(populacao, mae)
        # CRUZAMENTO

        # usando a notação de slice reduzido, o valor de
        # parada (segundo parametro dentro das chaves) é
        # igual a 'b - 1'. Portanto para que ele pare no 
        # ponto exato 10 é necessário colocar o valor de 
        # b como b+1, nesse caso 11, ou 21 (ja que o 
        # tamanho do cromossomo é de 20 genes)

        # separa os genes do pai e da mae
        a = ponto_de_cruzamento; b = total_de_genes
        # gera dois filhos, cada um com as partes complementares de cada pai
        cromossomo_filho1 = cromossomo_pai[0:(b-a)] + cromossomo_mae[a:b]
        cromossomo_filho2 = cromossomo_mae[0:(b-a)] + cromossomo_pai[a:b]
        # genes_paterno = cromossomo_pai[0:10]
        # genes_materno = cromossomo_mae[10:20]

        populacao_filhos.append(cromossomo_filho1)
        populacao_filhos.append(cromossomo_filho2)

        #DEBUG----------------------------------------------------------------
        #print('♂-----------------------------PAI-----------------------------')
        #print(f'{cromossomo_pai}\n')
        #print('♀-----------------------------MAE-----------------------------')
        #print(f'{cromossomo_mae}\n')
        #---------------------------------------------------------------------
        i += 1
    #DEBUG
    #print(*populacao_filhos, sep='\n')
    mutacao(populacao_filhos, taxa_de_mutacao)
    aptidao_filhos = porcentagem_da_aptidao(populacao_filhos)
    #DEBUG
    #mostrar_populacao_aptidao(populacao_filhos,aptidao_filhos)
    for filho in populacao_filhos:
        populacao.append(filho)
    for aptidao in aptidao_filhos:
        lista_de_aptidoes.append(aptidao)
### FUNCTION ---FUNÇÃO DE MUTAÇÃO---
# Essa é a função responsável pela diversidade de genes  
# na população de filhos, uma vez que todos eles possuem 
# partes que já existiam nos cromossomos pais. A mutação 
# garante que pelo um gene de um número de filhos (baseado
# na taxa de mutação) seja alterado (de 0 para 1 e de 1 para
# 0). Assim garantindo cromossomos completamente novos.
#### 
def mutacao(populacao_filhos, taxa_de_mutacao):
    for i in range(taxa_de_mutacao):
        index_escolhido = random.randint(0, len(populacao_filhos) - 1)
        escolhido = populacao_filhos[index_escolhido]

        index_gene_escolhido = random.randint(0, len(escolhido) - 1)
        if  (escolhido[index_gene_escolhido]) == 1:
            escolhido[index_gene_escolhido] = 0
        elif (escolhido[index_gene_escolhido]) == 0:
            escolhido[index_gene_escolhido] = 1
### FUNCTION ---FUNÇÃO DE SUBSTITUIÇÃO---
# Essa função garante que apenas os individuos com melhores
# fitness se mantenham para a próxima geração. Para isso 
# Precisamos saber o tamanho da população dada e quantidade 
# de filhos gerados em numeros inteiros. Após isso perocorremos
# os elementos menos aptos da lista e os eliminados (dada a 
# quantidade de filhos gerados). Ficando assim apenas os elementos
# mais aptos compondo o tamanho de população dado.
###
def substituicao(populacao, lista_de_aptidao, tamanho_populacao, taxa_de_cruzamento):
    n_filhos = math.floor(tamanho_populacao * taxa_de_cruzamento) 
    
    for i in range(n_filhos):
        menor = min(lista_de_aptidao)
        index_menor = lista_de_aptidao.index(menor)
        #print('index removidos:', index_menor)
        lista_de_aptidao.pop(index_menor)
        populacao.pop(index_menor)

    mostrar_populacao_aptidao(populacao, lista_de_aptidao)

def geracao(populacao, lista_de_aptidoes, tamanho_populacao, taxa_de_cruzamento, taxa_de_mutacao, taxa_de_geracoes):

    for i in range(taxa_de_geracoes - 1):
        cruzamento(populacao, lista_de_aptidoes, taxa_de_cruzamento, taxa_de_mutacao)
        
        substituicao(populacao, lista_de_aptidoes, tamanho_populacao,  taxa_de_cruzamento)

        j = 0
        for aptidao in lista_de_aptidoes:
            if aptidao > 100:
                mostrar_populacao_aptidao(populacao, lista_de_aptidoes)
                individuo_apto = populacao[j]
                print('[SIMULAÇÃO INTERROMPIDA]')
                return print('Foi encontrado algum individuo com mais de 100 de fitness nessa geração')
            j += 1
    print('[SIMULAÇÃO FINALIZADA]')
    j = 0
    for aptidao in lista_de_aptidoes:
            if aptidao > 100:
                # individuo_apto = populacao[j]
                return print('E foi encontrado um individuo com mais de 100 fitness nesse experimento')
            j += 1
    return print('E não foi encontrado nenhum individuo com mais de 100 fitness. Mude os parâmetros ou tente novamente')
### FUNCTION ---FUNCAO ENCONTRA CROMOSSOMO--
# Uma função basica para se encontrar um cromossomo
# na população tendo sendo index e a população 
###
def encontra_cromossomo(populacao, index):
    cromossomo = populacao[index]

    return cromossomo
def main():
    # CODIFICAÇÃO
    tamanho_cromo = 20
    # PARAMETROS DO ALGORITMO
    ## tamanho da população
    tamanho_pop = 10
    ## taxa de cruzamento (%)
    t_cruzamento = 0.4
    ## taxa de mutação (inteiro)
    taxa_de_mutacao = 1
    ## numero de geracoes
    taxa_de_geracoes = 6
    # lista de cromossomos (aka populacao)
    populacao = criar_populacao_inicial(tamanho_pop, tamanho_cromo)
    
    # esse algoritmo genetico utiliza de uma amostragem
    # estocastica para definir quais elementos serão 
    # selecionados para o cruzamento. Nisso, usaremos 
    # o método da roleta para escolher quais os individuos
    # cruzarão, garantindo a nova geração da população 

    # lista de aptidoes dos cromossomos
    aptidoes = porcentagem_da_aptidao(populacao)
    # aqui verificamos se a população inicial cumpre o 
    # criterio minimo que é de não ter todos os elementos
    # com aptidão zero, caso isso aconteça a população 
    # precisa ser reiniciada e portanto as aptidões devem
    # ser novamente avaliadas.
    ### VERIFICACAO da populacao inicial
    while(sum(aptidoes) == 0):
        populacao = criar_populacao_inicial(tamanho_pop)
        aptidoes = porcentagem_da_aptidao(populacao)
    
    geracao(populacao, aptidoes, tamanho_pop, t_cruzamento, taxa_de_mutacao, taxa_de_geracoes)
    # cruzamento(populacao, aptidoes, t_cruzamento, taxa_de_mutacao)
    # # populacao anterior mais o seus filhos
    # mostrar_populacao_aptidao(populacao, aptidoes)

    # substituicao(populacao, aptidoes, tamanho_pop,  t_cruzamento)

    #DEBUG------------------------------------
    #print(aptidoes) 
    #-----------------------------------------
## Funções de debug 
def mostrar_populacao(populacao):
    i = 1
    print('--------------------------------------------------------------')
    for individuo in populacao:
        print(f'Cromossomo {i}:')
        print(f'{individuo}')
        i += 1
    print('--------------------------------------------------------------')

def mostrar_populacao_aptidao(populacao, aptidoes):
    i = 0
    print('\n')
    for individuo in populacao:
        print(f'Cromossomo {i+1}:')
        print(f'{individuo} [RESULTADO]: {aptidoes[i]} de fitness', end='\n')
        i += 1
    print('\n')

def mostrar_individuo_apto(populacao, aptidoes, individuo):
    index = populacao.index(individuo)
    aptidao = aptidoes[index]
    print('O individuo com mais de 100 de fitness é:')
    print(individuo, end=' ')
    print(f'[RESULTADO]: {aptidao} de fitness', end='\n')

main()