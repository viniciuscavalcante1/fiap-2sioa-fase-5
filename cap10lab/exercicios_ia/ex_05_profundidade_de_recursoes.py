"""Escreva uma função recursiva chamada contagem_regressiva
que recebe um número inteiro positivo como argumento e imprime
uma contagem regressiva a partir desse número até 1.
A função deve exibir a profundidade de cada chamada."""


def contagem_regressiva(n: int, profundidade: int):
    if n == 0:
        return
    print(f"Profundidade {profundidade}: {n}")
    contagem_regressiva(n - 1, profundidade + 1)
