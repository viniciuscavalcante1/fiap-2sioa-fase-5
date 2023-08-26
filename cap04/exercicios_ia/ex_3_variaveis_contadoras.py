"""Exercício 3 - Variáveis Contadoras:
Escreva um programa em Python que peça ao usuário para digitar 10 números e, em seguida,
imprima a quantidade de números positivos, negativos e iguais a zero que foram digitados.
"""

quantidade_positivos = 0
quantidade_negativos = 0
quantidade_zero = 0

print("Insira 10 números, por favor: ")
for i in range(11):
    numero = int(input())
    if numero > 0:
        quantidade_positivos += 1
    elif numero < 0:
        quantidade_negativos += 1
    else:
        quantidade_zero += 1
print(f"Dos números que digitou, {quantidade_positivos} são positivos, {quantidade_negativos} são"
      f" negativos e {quantidade_zero} são zero.")
