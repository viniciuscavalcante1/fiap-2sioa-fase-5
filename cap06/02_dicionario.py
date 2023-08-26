dicionario = {}
print(type(dicionario))

dicionario = {
    "Yoda": "Mestre Jedi",
    "Mace Windu": "Mestre Jedi",
    "Anakin Skywalker": "Cavaleiro Jedi",
    "R2-D2": "Droide",
    "Dex": "Balconista"
}

print(dicionario)

print(f"Values: {dicionario.values()}")
for valor in dicionario.values():
    print(valor)

print(f"Keys: {dicionario.keys()}")
for chave in dicionario.keys():
    print(chave)

print(dicionario["R2-D2"])

print(dicionario.items())
for chave, valor in dicionario.items():
    print(f"{chave} -- {valor}")

dicionario["Vi"] = "Desenvolvedor"

nome_colaborador = input("Por favor, informe o nome do colaborador: ")
cargo_colaborador = input("Por favor, informe o cargo do colaborador: ")
dicionario[nome_colaborador] = cargo_colaborador

dicionario.pop("Mace Windu")
dicionario.popitem()
for nome, cargo in dicionario.items():
    print(nome, cargo)

dicionario.clear()
print(dicionario)

contatos = {
    "Clark Kent": {
        "Celular": 123456,
        "E-mail": "clark@krypton.com"
    },
    "Bruce Wayne": {
        "Celular": 654321,
        "E-mail": "bat@caverna.com"
    }
}

for nome, formas_contato in contatos.items():
    for forma, valor in formas_contato.items():
        print(nome, forma)