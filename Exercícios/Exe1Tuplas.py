#Um programa com uma única tupla com nomes de produtos e seus respectivos preços. Apresentar os dados de forma
#tabular e identados.

print(f"Olá! Digite o nome e preço dos 5 produtos respectivamente: ")

Produtos = (input(),float(input()),
            input(),float(input()),
            input(),float(input()),
            input(),float(input()),
            input(),float(input()))

var = "TABELA DE PREÇOS"
print('=' * 50)
print('{:=^50}' .format(var))
print('=' * 50)

for i in range(0,len(Produtos)):
    if i % 2 == 0:
        print(f'= {Produtos[i]:.<37}', end='')
    else:
        print(f'R${Produtos[i]:>7.2f} =')

print('=' * 50)