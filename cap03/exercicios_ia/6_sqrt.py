"""Biblioteca math e método math.sqrt:
Faça um programa que peça ao usuário um valor positivo e calcule a raiz quadrada desse valor
utilizando a biblioteca math. Caso o usuário digite um valor negativo, exiba uma mensagem de erro.
"""
import math
numero = int(input("Digite um número positivo: "))
if numero > 0:
    print(f"Raiz quadrada de {numero} é {math.sqrt(numero)}.")
else:
    print("Erro. Você digitou um número negativo.")
