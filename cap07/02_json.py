import json

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


arquivo = open("dicionario.json", "w", encoding="UTF-8")
conteudo = json.dumps(contatos, indent=4)
arquivo.write(conteudo)
arquivo.close()

# json para dicionario
arquivo = open("dicionario.json", encoding="UTF-8")
conteudo = arquivo.read()
agenda = json.loads(conteudo)
print(agenda)
arquivo.close()

# with
# arquivo = open(path)
# arquivo.close()

with open("dicionario.json") as arquivo:
    print(arquivo.read())

with open("dicionario.json", "w") as arquivo:
    arquivo.write("eita")