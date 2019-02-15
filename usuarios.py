
# git add .
# git commit -m 'Exercicio final da aula 3'
# git push origin master

users = list()
for l in open('usuarios.csv'):
    nome, idade, email = l.split(',')
    u = {
        "nome" : nome.strip(),
        "email" : email.strip(),
        "idade" : int(idade.strip())
    }
    users.append(u)

# Colocar todos os usuários dentro de uma lista
# Percorrer essa lista, exibindo apenas o nome de cada um

def unpack_user(u):
    n, i, e = u.split(',')
    return {
        'nome': n.strip(),
        'email': e.strip(),
        'idade': int(i.strip())
    }

users = [ unpack_user(u) for u in open('usuarios.csv') ]

for u in users:
    print(u['nome'])

# Ordernar todos os dicionários de uma vez pela chave nome

import json
print(json.dumps(sorted(map(unpack_user, open('usuarios.csv')), key=lambda o: o['nome']), indent=2))
