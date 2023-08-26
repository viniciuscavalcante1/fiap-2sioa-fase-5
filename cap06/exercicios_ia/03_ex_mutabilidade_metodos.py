"""Crie um dicionário de listas de tarefas,
 onde cada chave é um dia da semana
 e o valor é uma lista de tarefas para esse dia.
  Implemente uma função que permita adicionar tarefas a um dia específico.
"""

lista_de_tarefas = {
    "Segunda": ["Arrumar a casa", "Correr"],
    "Terça": ["Ir ao médico"],
    "Quarta": ["Entregar trabalho da faculdade", "Estudar Python"],
    "Quinta": ["Happy hour com o time", "Pagar boletos"],
    "Sexta": ["Limpar a casa", "Entregar projeto do trabalho"],
    "Sábado": ["Descansar"],
    "Domingo": ["Descansar"]
}


def adicionar_tarefas(dicionario: dict, dia_da_semana: str, tarefa: str) -> dict:
    dicionario[dia_da_semana].append(tarefa)
    return dicionario


print(adicionar_tarefas(lista_de_tarefas, "Segunda", "Ir para o escritório"))


"""Escreva um programa que utiliza um dicionário para contar a frequência
 de cada letra em uma determinada frase.
"""


def contar_frequencia_letra(frase: str) -> dict:
    return {letra: frase.count(letra) for letra in frase}


print(contar_frequencia_letra("aaaaaabbbbbb"))


"""Crie uma função que recebe um dicionário de estoque de produtos e uma lista de produtos
 a serem removidos. A função deve atualizar o estoque, removendo os produtos da lista.
"""

estoque = {
    "Prato": 10,
    "Copo": 7
}


def remover_estoque(dicionario: dict, produtos: list) -> dict:
    for produto in produtos:
        dicionario[produto] = dicionario[produto] - 1
    return dicionario


print(remover_estoque(estoque, ["Prato", "Copo"]))


"""Implemente um dicionário de contatos, onde cada chave é o nome de uma pessoa
 e o valor é uma lista de números de telefone. Crie funções para adicionar novos contatos, 
 remover contatos e atualizar números de telefone.
"""

contatos = {
    "Vi": 1234,
    "Kleb": 3402,
    "Nani": 1919
}


def adicionar_contato(dicionario_contatos: dict, nome: str, numero: int) -> dict:
    dicionario_contatos[nome] = numero
    return dicionario_contatos


def remover_contato(dicionario_contatos: dict, nome: str) -> dict:
    dicionario_contatos.pop(nome)
    return dicionario_contatos


def atualizar_contato(dicionario_contatos: dict, nome: str, numero_novo: int) -> dict:
    dicionario_contatos[nome] = numero_novo
    return dicionario_contatos


print(f"Adicionar contato: {adicionar_contato(contatos, 'Claudio', 9567)}")
print(f"Remover contato: {remover_contato(contatos, 'Nani')}")
print(f"Atualizar contato: {atualizar_contato(contatos, 'Vi', 4242)}")