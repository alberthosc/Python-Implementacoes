# Cadastre n pessoas identificadas pelo nome e peso, identifique o
# total de pessoas, o(s) mais pesado(os) e o(s) mais leve(es).
# Deve-se utilizar listas em listas para armazenar os dados.

pessoas = list()
dados = list()
quant = 0

# Definição da lista pelo usuário:
while True:
    dados.append(str(input(f'Digite o nome do indivíduo: ')))
    dados.append(float(input(f'Digite o peso do {dados[0]} em Kg: ')))
    quant +=1
    pessoas.append(dados[:])
    dados.clear()
    while True:
        aux = input(f'Desejas cadastrar outro indivíduo? (S/N): ')
        aux = aux.upper()
        if aux == 'S' or aux == 'N':
            break
        print(f'Não entendi. Por favor, repita!')
    if aux == 'N':
        break
    
peso_Pesado = 0.0
peso_Leve = 0.0
Mpesados = list()
Mleves = list()

#Definindo os mais pesados e os mais leves por Trono
for c in range(0,quant):
    if pessoas[c][1] >= peso_Pesado:
        peso_Pesado = pessoas[c][1]
        peso_Leve = pessoas[c][1]
for c in range(0,quant):
    if pessoas[c][1] <= peso_Leve:
        peso_Leve = pessoas[c][1]

#Criando a lista dos mais pesados (e mais leves), caso exista mais de um com o maior peso (e menor peso)        
for c in range(0, quant):
    if pessoas[c][1] == peso_Pesado:
        Mpesados.append(pessoas[c][0])
for c in range(0,quant):
    if pessoas[c][1] == peso_Leve:
        Mleves.append(pessoas[c][0])

print('=' * 52)
print(f'= Existe um total de {quant: ^5} indivíduos cadastrados! =')
print('=' * 52)

if peso_Pesado == peso_Leve:
    print(f'Todos os indivíduos possuem o mesmo peso!')
else:
    print(f'O(Os) indivíduo(os) mais pesado(os) é(são): ', end='')
    print(f'{Mpesados} ', end='')
    print(f'com {peso_Pesado}Kg.')
    print(f'\nO(Os) indivíduo(os) mais leve(os) é(são): ', end='')
    print(f'{Mleves} ', end='')
    print(f'com {peso_Leve}Kg.')

    

