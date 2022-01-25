print("Digite seu nome: ")
nome = input()
print("Olá, {}! Digite um valor:" .format(nome))
A1 = int(input())
print("Digite um segundo valor:")
A2 = int(input())
A3 = A1+A2
print("A soma de {} com {} equivale a : {}." .format(A1, A2, A3))
# Irá imprimir o nome centralizado dentro de 50 espaços
print("Foi um prazer, {: ^50} !" .format(nome))

#Função del para deletar uma variável:
del(A3)
print(A3) #Dirá que a variável não foi declarada