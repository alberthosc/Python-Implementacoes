# Tuplas: são similares a listas, isto é, uma sequência de dados de qualquer tipo. Um exemplo de Tuplas é "Animais"

Animais = ('Gatos', 'Cachorros', 'Macacos', 'Ratos')

for i in range(0, len(Animais)):
    print(f'Estes são mamíferos: {Animais[i]}')
    if (i == 4):
        break

print(f'\nOutro modo:\n')

for i in Animais:
    print(f'Estes são mamíferos: {i}')

print(f'\nOutro modo:\n')

for pos, conteudo in enumerate(Animais):
    print(f'Estes são mamíferos: {conteudo}, na posição: {pos}')

#Alguns métodos do objeto Tupla:
print(f'\nMétodos para o objeto do tipo Tupla criado:\n')

print('Em que posição estão os Macacos? {}' .format(Animais.index('Macacos'))) # .index
print('Existem Gatos nessa tupla? (1 para sim e 0 para não): {}' .format(Animais.count('Gatos'))) # .count