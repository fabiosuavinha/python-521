#!/usr/bin/python3

# grep -RHn <name>

duck_tails = ['Huguinho|1', 'Zezinho|2', 'Luizinho|3']

# Percorrer a variável duck_tails
# e exibir apenas os nomes, sem os números

for duck in map(lambda o: o.split('|')[0], duck_tails):
  print(duck)

# Ao invés de escrever o nome todo,
# escrever a primeira e a última letra de cada nome

for duck in map(lambda o: o.split('|')[0], duck_tails):
  if duck != 'Zezinho':
    print('{} {}'.format(duck[0], duck[-1]))

# transformar o double em lambda
for n in map(lambda x: x * 2, range(1, 5)):
  print(n)