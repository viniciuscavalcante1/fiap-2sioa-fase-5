"""Escreva um programa que itere sobre as chaves de um
 dicionário de filmes e imprima o nome de cada filme.
"""

filmes = {
    "Toy Story": 1990,
    "Toy Story 2": 1999
}

for filme in filmes.keys():
    print(filme)


"""Crie um dicionário que contenha palavras como chaves
 e suas respectivas definições como valores. 
 Em seguida, implemente uma função que retorne uma lista
  de todas as palavras do dicionário.
"""

palavras = {
    "bola": "objeto redondo",
    "garrafa": "objeto para estocar líquidos"
}


def lista_palavras_dicionario(dicionario: dict) -> list:
    return list(dicionario.keys())


print(lista_palavras_dicionario(palavras))


"""Crie um dicionário de dicionários que represente
 informações sobre livros (título, autor, ano).
  Implemente uma função que receba o dicionário 
  e retorne uma lista com os títulos dos livros.

"""

livros = {
    "O pequeno príncipe": {
        "Autor": "Antoine",
        "Ano": 1960
    },
    "Can't hurt me": {
        "Autor": "Goggins",
        "Ano": 2018
    }
}


def lista_livros(dicionario: dict) -> list:
    return list(dicionario.keys())


print(lista_livros(livros))


"""Escreva uma função que recebe um dicionário de ingredientes
 e seus respectivos preços.
  A função deve calcular e retornar o preço médio dos ingredientes.

"""

ingredientes = {
    "Arroz": 17,
    "Açúcar": 6,
    "Água": 2
}


def media_ingredientes(dicionario_ingredientes: dict) -> float:
    return sum(dicionario_ingredientes.values()) / len(dicionario_ingredientes.values())


print(media_ingredientes(ingredientes))