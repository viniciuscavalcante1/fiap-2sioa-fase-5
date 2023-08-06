"""Transporte-se no tempo e volte para a época de escola! Lembra do dia em que aprendeu
a encontrar o valor de x nas equações de segundo grau? Aquelas que tinham uma carinha parecida
com ax² + bx + c = 0?

Aquela fórmula que aprendemos como fórmula de Bhaskara (mas que não foi ele quem criou) deixou
saudades (ou pesadelos terríveis).

Vamos dar um presente ao seu "eu" do passado e criar um programa no qual o usuário só tenha que
escrever os valores de A, B e C e nosso programa vai se encarregar de fazer os cálculos.

A primeira etapa que aprendemos na escola é calcular o delta por meio da fórmula B² - 4 * a * c.
Depois, caso o delta seja positivo, existem 2 valores para x. Caso seja zero, existe apenas um
valor. E caso seja negativo, informamos não haver valor real para x."""

"""Agora, dentro dos desvios, incluiremos os cálculos de x. A fórmula que aprendemos na escola
é x = (-b +- sqrt(b² - 4ac)/2a), na qual o que está dentro da raiz é o delta, que já calculamos
anteriormente.

E por falar em raiz, cada linguagem de programação possui sua função própria para realizar essa
operação. No caso do Python precisamos importar a classe math e depois usar a função math.sqrt"""

import math

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = b * b - 4 * a * c

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"x1: {x1}")
    print(f"x2: {x2}")

elif delta == 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    print(f"x1: {x1}")

else:
    print("Não há valor real para x.")


