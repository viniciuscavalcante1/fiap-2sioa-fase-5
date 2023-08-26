"""F-strings e Função float():
a) Escreva um programa que peça ao usuário para digitar a temperatura em graus Celsius e, em seguida, converta-a para graus Fahrenheit utilizando f-strings para formatar a saída com duas casas decimais."""

celsius = float(input("Por favor, insira a temperatura em celsius: "))
fahrenheit = (celsius * 1.8) + 32
print(f"A temperatura em fahrenheit é {fahrenheit:.2f}")