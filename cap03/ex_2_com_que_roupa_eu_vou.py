"""Uma loja virtual que vende roupas personalizadas, disponibilizou no mês do seu aniversário
o cupom NIVER10 que concede 10% de desconto no valor total de uma compra feita no site.

Caso o cliente digite o cupom corretamente, deverá ser informado do valor final da compra
já com o desconto aplicado. Caso digite qualquer cupom incorreto, deverá ser informado
do valor da compra sem o desconto.
"""

cupom = "NIVER10"
desconto = 0.9

valor_compra = float(input("Digite o valor da compra: "))
cupom_cliente = input("Digite o cupom de desconto: ").upper()

if cupom_cliente == cupom:
    valor_compra *= desconto

print(f"O valor final da compra será de R${valor_compra}.")