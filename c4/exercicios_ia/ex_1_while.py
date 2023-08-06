"""Exercício 1 - Loops While:
Escreva um programa em Python que solicite ao usuário um número inteiro positivo
e imprima todos os números pares de 0 até o número digitado, usando um loop while.
"""

numero = int(input("Por favor, insira um número inteiro positivo: "))
i = 0
while i <= numero:
    if i % 2 == 0:
        print(i)
    i += 1
