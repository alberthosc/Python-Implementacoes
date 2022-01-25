pontos = 5

arquivo = open('recorde.txt', 'w')


arquivo.write('2')
arquivo.close()

arquivo = open('recorde.txt', 'r')
recorde = arquivo.read()
print(recorde)

recorde = int(recorde)

if pontos >= recorde:
    arquivo = open('recorde.txt', 'w')
    arquivo.write(str(pontos))


arquivo.close()