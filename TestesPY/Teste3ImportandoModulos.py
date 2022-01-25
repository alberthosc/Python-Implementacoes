import emoji
import math

#Abre o terminal e digita "pip install NOME DA BIBLIOTECA"

print("Digite seu nome: ")
nome = input()
print("Olá, {}! Digite um valor:" .format(nome))
A1 = int(input())
raiz = math.sqrt(A1)
print("A raiz quadrada de {} equivale a: {}" .format(A1, math.sqrt(A1)))
print("A raiz quadrada de {} com 2 casas decimais equivale a: {:.2f}" .format(A1, raiz))
print("A raiz quadrada de {} arredondado para cima equivale a: {}" .format(
    A1, math.floor(raiz)))
print("A raiz quadrada de {} arredondado para cima equivale a: {}" .format(
    A1, math.floor(math.sqrt(A1))))

print(emoji.emojize("Obrigado! :sunglasses:", use_aliases=True))
