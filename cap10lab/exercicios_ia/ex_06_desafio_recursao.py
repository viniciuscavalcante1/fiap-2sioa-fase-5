"""Implemente uma função recursiva chamada soma_digitos
que calcula a soma dos dígitos de um número inteiro.
Por exemplo, a soma dos dígitos de 123 é 6 (1 + 2 + 3)."""


def soma_digitos(n: int) -> int:
    if len(str(n)) == 1:
        return n
    return int(str(n)[0]) + soma_digitos(int(str(n)[1:]))


print(soma_digitos(123))