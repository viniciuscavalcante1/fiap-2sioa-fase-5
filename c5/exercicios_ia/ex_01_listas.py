"""Crie uma lista vazia chamada numeros e utilize o método append()
 para adicionar os números de 1 a 5 a essa lista.
 Imprima a lista resultante."""

numeros = []
for i in range(1, 6, 1):
    numeros.append(i)
print(numeros)

"""Utilize o método insert() para adicionar o número 10 na segunda posição da lista numeros.
 Imprima a lista atualizada."""

numeros.insert(1, 10)
print(numeros)

"""Utilize os métodos pop() e remove()
 para remover o último elemento da lista numeros e o número 3, respectivamente.
  Imprima a lista após cada remoção."""
numeros.pop()
print(numeros)
numeros.remove(3)
print(numeros)

"""Crie uma nova lista chamada duplicados contendo alguns números repetidos.
 Use o método count() para contar quantas vezes o número 5 aparece na lista."""
duplicados = [1, 1, 1, 1, 1, 1, "teste", 5, 5, 5]
print(duplicados.count(5))

"""Ordene a lista numeros em ordem decrescente usando o método sort() e,
 em seguida, reverta a ordem dos elementos usando o método reverse().
  Imprima a lista após cada operação."""
numeros.sort(reverse=True)
print(numeros)
numeros.reverse()
print(numeros)