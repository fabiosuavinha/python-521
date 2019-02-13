#!/usr/bin/python3

usuarios = [{"nome": "Hector", "idade" : 27, "email" : "hector.silva@4linux.com.br"},
{"nome": "Leonel", "idade" : 50,"email" : "leoneldesouza@gmail.com", 'filhos' : ['Ana', 'João', 'Antônio']},
{"nome": "Hugo", "idade" : 36, "email" : "hleosousa@bol.com.br"},
{"nome": "Guilherme Serafim", "idade" : 27, "email" : "guisilvaserafim@gmail.com"},
{"nome": "Joel", "idade" : 28, "email" : "oliveira.shiai@yahoo.com.br"},
{"nome": "Ayron", "idade" : 28, "email" : "ayron_pedro@hotmail.com", 'filhos' : ['Belzebu', 'Belphegor', 'Baphomet']},
{"nome": "Lucas", "idade" : 25, "email" : "lucas.salles@4linux.com.br"},
{"nome": "Roger", "idade" : 23, "email" : "rogeralexandre95@gmail.com"},
{"nome": "Victor Lapetina", "idade" : 23, "email" : "victor.lrs95@gmail.com"},
{"nome": "Cicero", "idade" : 52, "email" : "jose.cicero@gmail.com", 'filhos' : ['Nicko', 'Xiphorimphola']},
{"nome": "Daniel", "idade" : 37, "email" : "danylemis@yahoo.com.br"},
{"nome": "Fabiano", "idade" : 36, "email" : "fabianobat@gmail.com"},
{"nome": "Flavio", "idade" : 43, "email" : "flaviogpacheco@hotmail.com", 'filhos' : ['Pedro', 'Paulo', 'Peterson']},
{"nome": "Guilherme Ayres", "idade" : 23, "email" : "gui.ayres@hotmail.com"}]

for u in usuarios:
    if 'filhos' in u:
        print(u['filhos'][0])

exit()
usuarios = [{"nome": "Hector", "idade" : 27, "email" : "hector.silva@4linux.com.br"},
{"nome": "Leonel", "idade" : 50,"email" : "leoneldesouza@gmail.com"},
{"nome": "Hugo", "idade" : 36, "email" : "hleosousa@bol.com.br"},
{"nome": "Guilherme Serafim", "idade" : 27, "email" : "guisilvaserafim@gmail.com"},
{"nome": "Joel", "idade" : 28, "email" : "oliveira.shiai@yahoo.com.br"},
{"nome": "Ayron", "idade" : 28, "email" : "ayron_pedro@hotmail.com"},
{"nome": "Lucas", "idade" : 25, "email" : "lucas.salles@4linux.com.br"},
{"nome": "Roger", "idade" : 23, "email" : "rogeralexandre95@gmail.com"},
{"nome": "Victor Lapetina", "idade" : 23, "email" : "victor.lrs95@gmail.com"},
{"nome": "Cicero", "idade" : 52, "email" : "jose.cicero@gmail.com"},
{"nome": "Daniel", "idade" : 37, "email" : "danylemis@yahoo.com.br"},
{"nome": "Fabiano", "idade" : 36, "email" : "fabianobat@gmail.com"},
{"nome": "Flavio", "idade" : 43, "email" : "flaviogpacheco@hotmail.com"},
{"nome": "Guilherme Ayres", "idade" : 23, "email" : "gui.ayres@hotmail.com"}]

print('NOME: {0:.>20} EMAIL: {1:.>40}'.format('', ''))
for u in usuarios:
    print('{0:.>26} {1:.>47}'.format(u['nome'], u['email']))

exit()
usuarios = [[1, '4Linux', 4], [5, 7, 'Python'], [9, 'c', 11, 12, 13]]
for u in usuarios:
    for i in u:
        if type(i) == str:
            print(i.upper())

exit()
letras = ['a','b','c','d']
v1, *v2 = letras
print(v2)
