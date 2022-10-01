#   Albertho Síziney Costa
#   30/09/2022
#   Implementação do método de busca em inteligência artificial A Star, com eurística euclidiana para os cálculos dos custos,
#   onde a entrada se dá através de um arquivo TXT com os dados do labirinto na primeira linha, e o próprio labirinto no
#   formato de matriz nas linhas seguintes.


from cmath import sqrt
import numpy as np
import math
from pickle import FALSE, TRUE

def Read_Txt():
    arquivo = input('Digite o nome completo do arquivo txt:')
    variaDiagonal = input('Deseja variar o custo diagonal? (S/N):')
    with open(f'{arquivo}', "r") as labirinto:
        texto = labirinto.readlines()  # Cria uma lista de strings para o conteúdo do txt
    variaveis = texto[0].split()    # Cria uma lista de string com cada elemento da primeira linha do txt

    global nl
    global nc
    global ch
    global cv
    global cd

    global inicio_X
    global inicio_Y
    global final_X
    global final_Y

    nl = int(variaveis[0])  # Numero de linhas
    nc = int(variaveis[1])  # Numero de colunas
    ch = int(variaveis[2])  # Custo horizontal
    cv = int(variaveis[3])  # Custo vertical

    if variaDiagonal == 'S' or variaDiagonal == 's':
        cd = float(input('Digite o valor do custo diagonal desejado: '))  # Custo diagonal
    else:
        cd = math.sqrt(pow(ch, 2)+pow(cv, 2))  # Custo diagonal

    inicio_X = 0
    inicio_Y = 0
    final_X = 0
    final_Y = 0

    # Cria uma lista de str com cada elemento de cada linha do txt (split) e adiciona em uma
    # outra lista (append) criando assim uma matriz com cada elemento do labirinto ("1,nl+1"
    # é o intervalo do FOR para não utilizar a primeira linha do TXT).
    matriz = []
    linha = []
    for i in range(1, nl+1):
        linha = texto[i].split()
        matriz.append(linha)

    # Encontra as posições referentes aos nós inicial e final.
    for linha in range(0, nl):
        for coluna in range(0, nc):
            matriz[linha][coluna] = int(matriz[linha][coluna])
            if (matriz[linha][coluna] == 2):
                inicio_Y = coluna
                inicio_X = linha
            elif (matriz[linha][coluna] == 3):
                final_Y = coluna
                final_X = linha
    return matriz


def Astar(labirinto):

    #   Heurística que define a dist. entre o nó atual e a chegada.
    def Heuristica(i, j): return (math.sqrt(pow(final_X - i, 2) + pow(final_Y - j, 2)))
    #   Valor do custo do movimento (ch,cv ou cd) + valor da heurística.
    def CustoTotal(ConteudoAtual): return ConteudoAtual[2] + ConteudoAtual[3]

    #   Lista com os dados da busca (tupla com as coordenadas atuais, anterior, movimento, heuristica)
    Conteudo = [((inicio_X, inicio_Y), list(), 0,
                 Heuristica(inicio_X, inicio_Y))]
    #   Discionário com os nós acessados (KEY) e seus respectivos custos (CustoTotal).
    Verificados = {}

    matrizCaminhos = labirinto
    matrizCaminhoFinal = labirinto
    auxiliarPrint = (nc*2-4)    #Valor de caracteres "-" para printar a matriz

    passo = 0
    while True:

        # Obtém o item atual na lista 'Conteudo', referente ao primeiro termo (no final do laço deve-se
        # reorganizar a lista 'Conteudo' deixando o termo de menor custo no inicio, assim o 'ConteudoAtual'
        # irá sempre obter o nó mais atualizado da busca (nó de menor custo)).
        ConteudoAtual = Conteudo.pop(0)

        # Verifica se a chegada foi encontrada.
        passo = passo + 1
        (i, j) = ConteudoAtual[0]
        if labirinto[i][j] == 3:
            # Insere no discionário de Verificados o último nó (pos e custo).
            Verificados[(i, j)] = (Conteudo[1][2])
            # Caminho partida x chegada (nó a nó)
            Rota = [ConteudoAtual[0]] + ConteudoAtual[1]
            Rota.reverse()  # Deixa o caminho em ordem crescente de nós (início ao fim)
            matrizCaminhos[ConteudoAtual[0][0]][ConteudoAtual[0][1]] = 'X'

            print(auxiliarPrint*'-', end='')
            print(F'PASSO {passo}', end='')
            print(auxiliarPrint*'-')
            for l in range(0, nl):
                for c in range(0, nc):
                    print(f'[{matrizCaminhos[l][c]:^2}]', end='')
                print()

            print((auxiliarPrint-3)*'-', end='')
            print('CAMINHO FINAL', end='')
            print((auxiliarPrint-3)*'-')    
            for pos in Rota:
                matrizCaminhoFinal[pos[0]][pos[1]] = 'V'
            for l in range(0, nl):
                for c in range(0, nc):
                    print(f'[{matrizCaminhoFinal[l][c]:^2}]', end='')
                print()
            return Rota,Verificados,Conteudo

        print(auxiliarPrint*'-', end='')
        print(F'PASSO {passo}', end='')
        print(auxiliarPrint*'-')
        matrizCaminhos[ConteudoAtual[0][0]][ConteudoAtual[0][1]] = 'X'
        for l in range(0, nl):
            for c in range(0, nc):
                print(f'[{matrizCaminhos[l][c]:^2}]', end='')
            print()

        # Adiciona ao discionário 'Verificados', a posição como KEY e o argumento como custo total.
        Verificados[(i, j)] = (ConteudoAtual[2] + ConteudoAtual[3])

        # Adicionando vizinhos do nó atual na lista 'Vizinhos'.
        Vizinhos = list()
        if i > 0 and (labirinto[i-1][j] == 0 or labirinto[i-1][j] == 2 or labirinto[i-1][j] == 3):
            Vizinhos.append((i-1, j))  # Add vizinho acima mesma coluna
        if i > 0 and j > 0 and (labirinto[i-1][j-1] == 0 or labirinto[i-1][j-1] == 2 or labirinto[i-1][j-1] == 3):
            Vizinhos.append((i-1, j-1))  # Add vizinho acima coluna à esquerda
        if i > 0 and j < nc - 1 and (labirinto[i-1][j+1] == 0 or labirinto[i-1][j+1] == 2 or labirinto[i-1][j+1] == 3):
            Vizinhos.append((i-1, j+1))  # Add vizinho acima coluna à direita
        if i < nl - 1 and (labirinto[i+1][j] == 0 or labirinto[i+1][j] == 2 or labirinto[i+1][j] == 3):
            Vizinhos.append((i+1, j))  # Add vizinho abaixo mesma coluna
        if i < nl - 1 and j > 0 and (labirinto[i+1][j-1] == 0 or labirinto[i+1][j-1] == 2 or labirinto[i+1][j-1] == 3):
            Vizinhos.append((i+1, j-1))  # Add vizinho abaixo coluna à esquerda
        if i < nl - 1 and j < nc - 1 and (labirinto[i+1][j+1] == 0 or labirinto[i+1][j+1] == 2 or labirinto[i+1][j+1] == 3):
            Vizinhos.append((i+1, j+1))  # Add vizinho abaixo coluna à direita
        if j > 0 and (labirinto[i][j-1] == 0 or labirinto[i][j-1] == 2 or labirinto[i][j-1] == 3):
            Vizinhos.append((i, j-1))  # Add vizinho mesma linha à esquerda
        if j < nc - 1 and (labirinto[i][j+1] == 0 or labirinto[i][j+1] == 2 or labirinto[i][j+1] == 3):
            Vizinhos.append((i, j+1))  # Add vizinho mesma linha à direita

        for n in Vizinhos:
            if (n[0] == i and (n[1] == j+1 or n[1] == j-1)):
                movimento = ch  # Se o vizinho estiver à esq. ou dir. na mesma linha
            elif (n[1] == j and n[0] != i):
                movimento = cv  # Se o vizinho estiver abaixo ou acima na mesma coluna
            elif (n[0] != i and n[1] != j):
                movimento = cd  # Se o vizinho estiver à esq. ou dir. em linhas diferentes

            # Valor heurístico + valor de movimentação
            ProximoCusto = (ConteudoAtual[3] + movimento)
            if n in Verificados and Verificados[n] >= ProximoCusto:
                continue
            Conteudo.append((n, [ConteudoAtual[0]] + ConteudoAtual[1],
                             ProximoCusto, Heuristica(n[0], n[1])))

        # Reorganiza a lista 'Conteudo' de acordo com o menor CustoTotal.
        Conteudo.sort(key=CustoTotal)

def Resultados(Rota,Verificados,TodosAcessados):
    
    print('\nO caminho obtido foi:')
    print(Rota)

    print('\nA lista com os nós Fechados e seus custos é:')
    for posRota in Rota:
        for posVerificados in Verificados:
            if (posRota) == (posVerificados):
                print(f'{posRota}: Custo --> {Verificados[posRota]}')

    naoRepete = list()
    print('\nA lista com os nós Abertos e seus custos é:')
    for posTodos in TodosAcessados:
        if posTodos[0] not in Rota and posTodos[0] not in naoRepete:
            naoRepete.append(posTodos[0])
            print(f'{posTodos[0]}: Custo --> {posTodos[3]}')
            

matriz = Read_Txt()
Rota,Verificados,TodosAcessados = Astar(matriz)
Resultados(Rota,Verificados,TodosAcessados)



