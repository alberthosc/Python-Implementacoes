# Listas em python

#Num = [9, 7, 4, 5, 3, 6, 2, 1, 0, 8]    #também usadas com colchetes
#Num.append(10)  # adiciona o valor 10 à lista
#print('\n', Num)
#Num.sort()  # ordena a lista
#print('\n', Num)
#Num.sort(reverse=True)  # ordena a lista de forma reversa
#print('\n', Num)
#Num.insert(2,11)    #adiciona o valor 11 à lista na posição 2
#print('\n', Num)
#Num.pop(2)    #retira o valor encontrado na posição 2
#print('\n', Num)
#Num.remove(8)    #retira o PRIMEIRO valor 8 encontrado na lista
#print('\n', Num)

Lista1 = [0,1,2,3]
Lista2 = Lista1

Lista2[1] = 4   #Ao fazer isso, é criada uma variável LISTA2 que busca o 
#mesmo espaço de memória de LISTA1, logo a alteração ocorre em ambas as listas

Lista3 = Lista1[:]  #Dessa forma é criada uma nova lista em um endereço de memória
#diferente, de forma que alterações nessa lista implica somente nela
Lista3[1] = 5

print(f'Lista 1: {Lista1}')
print(f'Lista 2: {Lista2}')
print(f'Lista 3: {Lista3}')