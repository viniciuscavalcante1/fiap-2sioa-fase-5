"""Crie uma função em Python que recebe uma tupla como
 parâmetro e retorna a quantidade de elementos na tupla."""


def len_tupla(tupla: tuple) -> int:
    return len(tupla)


print(len_tupla(("Teste", "Teste")))

"""Escreva um programa que cria um dicionário vazio e,
 em seguida, insere pares chave-valor representando nomes
  de frutas e suas quantidades."""

dicionario_frutas = {}
dicionario_frutas["abacaxi"] = 3
dicionario_frutas["melancia"] = 2
dicionario_frutas["uva"] = 4

print(dicionario_frutas)

"""Implemente uma função que recebe um dicionário de frutas 
e uma fruta específica para remover.
 A função deve retornar o dicionário após a remoção da fruta."""


def remover_fruta(dicionario: dict, fruta: str) -> dict:
    dicionario.pop(fruta)
    return dicionario


print(remover_fruta(dicionario_frutas, "abacaxi"))


"""Desempacote uma tupla contendo informações de um livro 
(título, autor, ano) e imprima cada uma das informações.
"""

tupla_livros = ("Livro", "Autor", 1950)
livro, autor, ano = tupla_livros
print(livro, autor, ano)


"""Crie uma função que recebe um dicionário de notas de alunos
 (nome do aluno como chave e nota como valor) e retorna a média das notas.
"""

notas_de_alunos = {
    "Vi": 10,
    "Carlos": 7,
    "Maria": 9,
    "João": 10
}


def media_alunos(dicionario_notas: dict) -> float:
    return sum(dicionario_notas.values()) / len(dicionario_notas.values())


print(media_alunos(notas_de_alunos))