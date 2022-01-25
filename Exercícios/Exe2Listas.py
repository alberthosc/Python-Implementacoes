# Digite n valores em uma lista e retorne o maior, menor e sua(as) respectiva(as) posição(ões)

print('Digite n valores inteiros para uma lista:')
lista = []
tronoMenor = 0
tronoMaior = 0
aux = 's'
i = 0

# Definição da lista pelo usuário:
while True:
    lista.append(int(input(f'Digite o valor da posição {i}: ')))
    while True:
        aux = input(f'Desejas acrescentar outro valor? (s/n): ')
        if aux == 's' or aux == 'n' or aux == 'S' or aux == 'N':
            break
        print(f'Não entendi. Por favor, repita!')

    if aux == 'n' or aux == 'N':
        break
    i = i+1

# Busca do MAIOR valor por TRONO
for num in lista:
    if num >= tronoMaior:
        tronoMaior = num
        tronoMenor = num

# Busca do MENOR valor por TRONO
for num in lista:
    if num <= tronoMenor:
        tronoMenor = num
        
print(
    f'O maior número encontrado na lista é: {tronoMaior}, na(s) posição(ções): ', end='')
for c, num in enumerate(lista):
    if num == tronoMaior:
        print(f'{c};', end='')

print(
    f'\nO menor número encontrado na lista é: {tronoMenor}, na(s) posição(ções): ', end='')
for c, num in enumerate(lista):
    if num == tronoMenor:
        print(f'{c};')
