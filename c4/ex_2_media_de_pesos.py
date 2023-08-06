"""No caminhão de uma empresa de transportes cabem exatamente 100 caixas de iguais dimensões.
O peso dessas caixas, porém, pode variar dependendo do seu conteúdo.

Como alguns caminhões têm se desgastado mais do que outros, você foi convocado para criar um algoritmo
que calcule o peso total das caixas que serão colocadas em um caminhão
e que exibia o peso médio das caixas.

A solução mais simples para isso é pedir que o usuário vá digitando o peso das caixas à medida
que elas são colocadas no caminhão (ou, futuramente, integrar nosso sistema com a balança).
Como sabemos que se trata de 100 caixas, podemos usar o loop for para nos ajudar!
"""

peso_total = 0.0
for i in range(1, 101):
    peso_total += float(input(f"Por favor, informe o peso da caixa {i}: "))
print(f"O peso total das 100 caixas é de {peso_total}kg e o peso médio por caixa é de {peso_total/100}")