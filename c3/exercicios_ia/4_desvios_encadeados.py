"""Desvios Condicionais Encadeados com If, Else e Elif:
Elabore um programa que peça ao usuário um número e verifique as seguintes condições:
a) Se o número for positivo, exiba "O número é positivo."
b) Se o número for negativo, exiba "O número é negativo."
c) Caso o número seja igual a zero, exiba "O número é zero."""

numero = int(input("Digite um número: "))
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")