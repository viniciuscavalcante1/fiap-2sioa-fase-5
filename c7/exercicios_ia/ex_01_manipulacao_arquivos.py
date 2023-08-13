"""Crie um programa que leia o conteúdo de um arquivo
 chamado "texto.txt" e exiba seu conteúdo na tela.
"""
with open('texto.txt', encoding='UTF-8') as arquivo:
    print(arquivo.read())


"""Escreva uma função que receba um nome de arquivo e
 um texto como parâmetros e escreva esse texto no arquivo,
  adicionando-o ao conteúdo existente.

"""


def escreva_texto_no_arquivo(nome_arquivo: str, texto: str):
    with open(f"{nome_arquivo}.txt", encoding='UTF-8', mode='a') as arquivo:
        arquivo.write(texto)


"""Escreva um programa que abra um arquivo em modo de escrita ("w")
 e escreva nele o seu nome e idade, utilizando acentuação,
  e salve-o com encoding UTF-8.
"""
with open("vi.txt", encoding="UTF-8", mode="w") as arquivo:
    conteudo = "Meu nome é Vinícius de Abreu Cavalcante e tenho 24 anos."
    arquivo.write(conteudo)


"""Crie uma função que leia um arquivo de texto em modo de leitura ("r")
 e conte quantas palavras começam com a letra 'A'.
"""
with open("vi.txt", encoding="UTF-8") as arquivo:
    linha = arquivo.readline()
    lista_palavras = linha.split()
    quantidade_a = 0
    for palavra in lista_palavras:
        if palavra[0] == "a":
            quantidade_a += 1
    print(f"O arquivo tem {quantidade_a} palavras com inicial 'a'")


"""Escreva um programa que leia o conteúdo de um arquivo e 
exiba apenas as linhas ímpares na tela.
"""

with open("parimpar.txt", encoding="UTF-8") as arquivo:
    lista_linhas = arquivo.readlines()
    len_arquivo = len(lista_linhas)
    for linha in range(len_arquivo):
        if linha % 2 == 0:
            print(lista_linhas[linha])


"""Desenvolva uma função que leia um arquivo linha por linha 
e retorne uma lista de strings, onde cada string contém o conteúdo 
de uma linha do arquivo.
"""


def lista_strings(arquivo: str) -> list:
    with open(arquivo, encoding="UTF-8") as a:
        return a.readlines()


"""Crie um programa que leia um dicionário contendo 
informações de livros (título, autor, ano) e escreva esses dados em 
um arquivo chamado "livros.json" no formato JSON.
"""

dicionario = {
    "TED Talks": {
        "Autor": "Dono do TED",
        "Ano": 2013
    },
    "Cant hurt me": {
        "Autor": "David Goggins",
        "Ano": 2018
    }
}

with open("livros.json", encoding="UTF-8", mode="w") as arquivo:
    import json
    json_dicionario = json.dumps(dicionario, indent=4)
    arquivo.write(json_dicionario)


"""Escreva uma função que leia o arquivo "livros.json", adicione um novo 
livro ao dicionário existente e atualize o arquivo.
"""

with open("livros.json", encoding="UTF-8") as arquivo:
    import json
    conteudo = arquivo.read()
    dicionario = json.loads(conteudo)
    dicionario["Python para análise de dados"] = {"Autor": "McKinney", "Ano": 2016}
    dicionario = json.dumps(dicionario, indent=4)

with open("livros.json", encoding="UTF-8", mode="w") as arquivo:
    arquivo.write(dicionario)


"""Crie um dicionário com informações sobre filmes (título, diretor, ano)
 e utilize o método json.dumps() com o parâmetro indent
  para criar uma versão formatada em JSON. 
  Em seguida, crie um novo dicionário a partir da string JSON 
  usando json.loads().
"""

dicionario = {
    "Star Wars: O Império Contra Ataca": {
        "Diretor": "George Lucas",
        "Ano": 1994
    },
    "Vingadores: Ultimato": {
        "Diretor": "Marvel",
        "Ano": 2019
    }
}

import json
json_arquivo = json.dumps(dicionario, indent=4)
dicionario_json = json.loads(json_arquivo)

"""Escreva um programa que abra um arquivo em modo de leitura, 
percorra cada linha e exiba apenas os primeiros 10 caracteres de cada linha.
"""
with open("parimpar.txt", encoding="UTF-8") as arquivo:
    lista_linhas = arquivo.readlines()
    for linha in lista_linhas:
        print(linha[:10])


"""Crie uma função que recebe uma string contendo uma frase e utiliza
 o método find() para encontrar a posição da primeira ocorrência da palavra
  "Python".
"""


def encontrar(frase: str) -> int:
    return frase.find("Python")


print(encontrar("O Python é muito bom"))