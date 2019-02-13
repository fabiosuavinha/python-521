#!/usr/bin/python3

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
operador = input('Digite o operador: ')

print(eval(f'{n1} {operador} {n2}'))

def soma(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult():
    pass

def div():
    pass

operacores = {'+' : soma, '-' : sub, '*' : mult, '/' : div}

