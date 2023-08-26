linguagens = ["Inglês", "Português"]
print(f"Linguagens antes de append: {linguagens}")
linguagens.append("Italiano")
print(f"Linguagens depois de append: {linguagens}")
linguagens.insert(0, input("Insira uma linguagem: "))
print(f"Linguagens: {linguagens}")
elemento_removido = [linguagens.pop()]
print(f"Linguagens depois do pop: {linguagens}")
print(f"Elemento removido: {elemento_removido}")
elemento_removido.append(linguagens.pop(0))
print(f"Linguagens após remover o primeiro elemento: {linguagens}")
print(f"Elemento removido: {elemento_removido[-1]}")