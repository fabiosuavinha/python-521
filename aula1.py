#!/usr/bin/python3

texto_grotesco = 'Por conseguinte, o novo modelo estrutural aqui preconizado nos obriga à análise das condições financeiras e administrativas exigidas. Ainda assim, existem dúvidas a respeito de como o surgimento do comércio virtual faz parte de um processo de gerenciamento das regras de conduta normativas. Neste sentido, a execução dos pontos do programa exige a precisão e a definição do fluxo de informações.'

nomes = ['Hector', 'Guilherme', 'Joel', 'Flávio', 'Fabiano', 'Roger', 'Cícero', 'Hugo', 'Ayron', 'Leonel', 'Pedro', 'Lucas']

if 'virtual' in texto_grotesco:
    print('Palavra "virtual" encontrada')

print(nomes[-4:])
print(len(texto_grotesco.split()))

for nome in nomes:
    # Mais elegante
    if nome[0] in 'FH':
        print(nome)
    # Segunda mais elegante
    if nome[0] == 'H' or nome[0] == 'F':
        print(nome)
    # A que funciona...
    if nome[0] == 'F':
        print(nome)
    elif nome[0] == 'H':
        print(nome)

# Percorrer a lista "nomes" e exibir apenas os nomes 
# que começam com a letra F e H
# for
# if com [:] em cima do item "do momento"

exit()
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

n3 = n1 + n2

# Se o numero for igual a 50, escrever "..."

if n3 > 100:
    print('Que número grandão...')
elif n3 == 50:
    print('...')
else:
    print('Que número pequeno...')
