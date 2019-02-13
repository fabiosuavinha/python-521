# print, len, str, format, int, input, range, enumerate

a = 'Olá global!'
def qualquer_coisa():
    a += ' Hum...'
    print(a)

qualquer_coisa()
print(a)

exit()
def square(n):
    return n**2

def par_impar(n):
    if n % 2 == 0:
        print('par')
    else:
        print('impar')

for i in range(0, 10):
    par_impar(i)

def reverse(i):
    return i[::-1]

letras = ['a', 'b', 'c', 'd', 'e']
print(reverse(letras))
