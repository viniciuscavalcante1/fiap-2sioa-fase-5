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


"""Desenvolva uma função que leia um arquivo CSV chamado
 "dados.csv" e retorne uma lista de dicionários,
  onde cada dicionário representa uma linha do arquivo com os
   cabeçalhos como chaves.
"""
