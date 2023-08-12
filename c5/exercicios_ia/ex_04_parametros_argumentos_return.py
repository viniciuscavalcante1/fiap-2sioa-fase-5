"""Escreva uma função chamada calculadora
 que recebe dois números e uma operação (+, -, *, /)
  como argumentos. A função deve realizar a operação
  especificada nos números e retornar o resultado.
"""


def calculadora(numero1: float, numero2: float, operacao: str) -> float:
    if operacao == "+":
        return numero1 + numero2
    elif operacao == "-":
        return numero1 - numero2
    elif operacao == "*":
        return numero1 * numero2
    elif operacao == "/":
        return numero1 / numero2
    else:
        print("Operação inválida")
