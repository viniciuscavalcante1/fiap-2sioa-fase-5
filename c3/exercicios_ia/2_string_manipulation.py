"""Métodos de Strings:
Escreva um programa que receba uma frase digitada pelo usuário e ofereça três opções de manipulação da frase:
a) Mostrar a frase em letras maiúsculas.
b) Mostrar a frase em letras minúsculas.
c) Exibir a frase dividida em palavras."""

frase = input("Digite uma frase: ")
opcao = input("Agora, escolha uma das opções: \na) Mostrar a frase em letras maiúsculas\nb) "
              "Mostrar a frase em letras minúsculas\nc) Exibir a frase dividida em palavras.").lower()
if opcao == 'a':
    print(f"Sua frase ficou assim: {frase.upper()}")
elif opcao == 'b':
    print(f"Sua frase ficou assim: {frase.lower()}")
else:
    print(f"Sua frase ficou assim: {frase.split()}")
