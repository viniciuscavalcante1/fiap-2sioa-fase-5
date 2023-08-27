"""Crie uma função recursiva chamada
 soma_recursiva que recebe uma lista de números
  e retorna a soma de todos os elementos da lista.
   Lembre-se de realizar a chamada recursiva corretamente."""


def soma_recursiva(lista: list):
    if not lista:
        return 0
    else:
        return lista[0] + soma_recursiva(lista[1:])
