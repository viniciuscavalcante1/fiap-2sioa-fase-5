"""Desvios Condicionais Simples e Compostos:
Crie um programa que solicite ao usuário sua idade.
Se a idade for maior ou igual a 18, exiba "Você é maior de idade." Caso contrário, exiba "Você é menor de idade."""

idade = int(input("Informe sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")