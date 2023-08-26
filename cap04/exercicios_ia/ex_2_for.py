"""Exercício 2 - Loops For:
Escreva um programa em Python que imprima a soma de todos os números ímpares entre 1 e 100,
usando um loop for.
"""

soma = 0
for i in range(1, 101, 2):
    soma += i
print(soma)
