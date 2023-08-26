def funcao_teste(v, n, limite):
    if n < limite:
        valor = float(input("informe valor: "))
        return funcao_teste(valor + v, n + 1, limite)
    else:
        return v


print(funcao_teste(1, 4, 1))