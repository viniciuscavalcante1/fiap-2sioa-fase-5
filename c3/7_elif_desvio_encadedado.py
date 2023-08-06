# Faixas de bônus
# > 1000 3 GB
# > 500 1,5 GB
# > 200 500 MB
# < 200 Nenhum bônus

pontos = int(input("Informe a quantidade de pontos do cliente: "))
if pontos > 1000:
    print(f"O cliente recebe 3 GB adicionais.")
elif pontos > 500:
    print("O cliente recebe 1,5 GB adicionais.")
elif pontos > 200:
    print("O cliente recebe 500 MB adicionais.")
else:
    print("O cliente não recebe nenhum bônus.")
