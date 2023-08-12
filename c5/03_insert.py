linguagens = ["Inglês", "Português"]
print(f"Linguagens antes de append: {linguagens}")
linguagens.insert(0, "Italiano")
print(f"Linguagens depois de append: {linguagens}")
linguagens.insert(0, input("Insira uma linguagem: "))
print(f"Linguagens: {linguagens}")