#!/usr/bin/python3

letras = [ 'a', 'Z', 'd', 'h', 'l', 'p', 'i', 'n', 't', 'o', 'A' ]

# Ordenar as letras e exibilas em maiúsculo

print('\nSol.: 1')
for l in map(lambda o: o.upper(), sorted(letras)):
  print(l)

print('\nSol.: 2')
for l in sorted(l.upper() for l in letras):
  print(l)

# Criar uma função que recebe uma letra qualquer
# e retorna esta letra em maiúsculo

def to_upper(l):
  return l.upper()

# Testar a função "to_upper"

assert 'A' == to_upper('a')

letras = [ 'a', 'Z', 'b', 'c', 'A' ]
ordenadas = sorted(letras, key=to_upper)

print('')
for l in ordenadas:
  print(l)

def merge_sort(collection, begin, end, predicate):

  mid = int(begin + (end-begin) / 2.0)

  if end-begin > 1:
    merge_sort(collection, begin, mid, predicate)
    merge_sort(collection, mid, end, predicate)

  left = [ collection[i] for i in range(begin, mid) ]
  right = [ collection[i] for i in range(mid, end) ]
  
  i, j, k = 0, 0, begin

  while i < (mid-begin) and j < (end-mid):
    if predicate(left[i]) <= predicate(right[j]):
      collection[k] = left[i]
      i = i + 1
    else:
      collection[k] = right[j]
      j = j + 1
    k = k + 1

  while i < (mid-begin):
    collection[k] = left[i]
    k = k + 1
    i = i + 1

  while j < (end-mid):
    collection[k] = right[j]
    k = k + 1
    j = j + 1


letras = [ 'a', 'Z', 'b', 'c', 'A' ]
merge_sort(letras, 0, len(letras), to_upper)

print(letras)
