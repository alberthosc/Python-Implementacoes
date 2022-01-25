# Manipulando uma estrutura de Lista de forma que sejam criadas outras estruturas que compõe listas
# Teste1, Teste2 e Teste3 são estruturas compostas
#---------------------------------------------------------
#---------------------------------------------------------
#teste1 = list()
# teste1.append('João')
# teste1.append(25)

#teste2 = list()
# teste2.append('Maria')
# teste2.append(31)

#teste3 = list()
# teste3.append(teste1[:]) #Lembrar de realizar o fatiamento completo "[:]" para fazer uma cópia com endereço distinto
# teste3.append(teste2[:])

# print(teste1)
# print(teste2)
# print(teste3)
#---------------------------------------------------------
#---------------------------------------------------------
#pessoas = [['Albertho', 22], ['Clarice', 19],
#          ['Beth', 39], ['Yvete', 61], ['Thay', 26]]
#print(pessoas[1][0])
#---------------------------------------------------------
#---------------------------------------------------------
pessoas = list()
dados = list()
for i in range(0,2):
    dados.append(str(input('Digite o nome da pessoa: ')))
    dados.append(int(input(f'Digite a idade de {dados[0]}: ')))
    pessoas.append(dados[:])
    print(pessoas)
    dados.clear()
#---------------------------------------------------------
#---------------------------------------------------------