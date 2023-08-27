"""Implemente uma função recursiva chamada potencia
 que calcula a potência de um número base
 elevado a um expoente. Certifique-se de incluir uma
 condição de parada para quando o expoente for igual a 0."""


def potencia(base, expoente):
    if expoente == 0:
        return 1
    else:
        return base * potencia(base, expoente - 1)
