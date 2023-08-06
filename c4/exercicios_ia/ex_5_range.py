"""Exercício 5 - Função range():
a) Escreva um programa em Python que imprima todos os números pares de 0 a 20
usando a função range().

b) Escreva um programa em Python que solicite ao usuário um número inteiro positivo
e imprima todos os números ímpares de 1 até o número digitado, usando a função range().
"""

for i in range(0, 21, 2):
    print(i)

numero = int(input("Por favor, insira um número inteiro positivo: "))
for i in range(1, numero + 1, 1):
    if i % 2 != 0:
        print(i)