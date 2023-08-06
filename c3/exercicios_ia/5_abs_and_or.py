"""Função abs() e operadores and e or:
Crie um programa que solicite ao usuário dois números inteiros e realize as seguintes verificações:
a) Se ambos os números forem positivos, exiba "Ambos os números são positivos."
b) Se ambos os números forem negativos, exiba "Ambos os números são negativos."
c) Se um dos números for zero, exiba "Pelo menos um dos números é zero."
d) Se nenhum dos números for zero, exiba "Nenhum dos números é zero."""

numero1 = int(input("Digite um número inteiro: "))
numero2 = int(input("Digite outro número inteiro: "))
if numero1 > 0 and numero2 > 0:
    print("Ambos os números são positivos.")
    print("Nenhum dos números é zero.")
elif numero1 < 0 and numero2 < 0:
    print("Ambos os números são negativos.")
    print("Nenhum dos números é zero.")
elif numero1 == 0 or numero2 == 0:
    print("Pelo menos um dos números é zero.")
