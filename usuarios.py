
# git add .
# git commit -m 'Exercicio final da aula 3'
# git push origin master

for l in open('usuarios.csv'):
    nome, idade, email = l.split(',')
    print({
        "nome" : nome.strip(),
        "email" : email.strip(),
        "idade" : int(idade.strip())
    })
