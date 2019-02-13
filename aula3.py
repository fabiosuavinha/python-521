#!/usr/bin/python3

#arquivo = open('zen.txt').read().upper()

arquivo = open('zen.txt')

# A linha nunca será apenas "-"
    # if ...
# enumerate
# mod -> 1 % 2 -> Se é par ou impar
# if 'belzebu' not in demonios:
# Printar apenas as linhas com palavras, ignorando as linhas com "-"

#i = 0
#for linha in arquivo:
#    linha = linha.strip()
#    if i % 2 == 0:
#        print(linha)
#    i = i + 1

for i, linha in enumerate(arquivo):
    if i % 2 == 0:
        print(linha.strip())
