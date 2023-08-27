"""Escreva uma função recursiva em Python chamada fatorial
 que recebe um número inteiro positivo como argumento
  e retorna o fatorial desse número.
"""


def fatorial(number: int):
    if number < 0:
        return None
    elif number == 0:
        return 1
    return number * fatorial(number - 1)
