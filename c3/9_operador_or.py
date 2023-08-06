# Uma loja concede descontos para compras pagas com cartão de crédito ou valor acima de R$100.

valor_compra = float(input("Por favor, informe o valor da compra: "))
forma_pagamento = int(input("Forma de pagamento, 1 para cartão de crédito e 2 para dinheiro: "))

if valor_compra > 100 or forma_pagamento == 1:
    valor_compra *= 0.9
    print("O cliente tem direito a desconto")

print(f"O valor da compra é de R${valor_compra}")
