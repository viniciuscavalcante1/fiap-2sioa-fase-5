"""Defina uma função chamada soma_pares que recebe
uma lista de números como argumento e retorna a soma dos números pares presentes na lista."""


def soma_pares(lista: list) -> float:
    pares = [numero for numero in lista if numero % 2 == 0]
    return sum(pares)


print(soma_pares([1, 2, 3, 4]))


"""Crie uma função chamada calcular_fatorial 
que recebe um número inteiro como argumento e retorna o fatorial desse número."""


def calcular_fatorial(numero: int) -> int:
    i = 1
    fatorial = 1
    while i <= numero:
        fatorial *= i
        i += 1
    return fatorial


print(calcular_fatorial(4))