from utils.NoDuplo import NoDuplo
from utils.ListaDuplamenteEncadeada import ListaDuplamenteEncadeada

lista = ListaDuplamenteEncadeada()
lista.adicionar_no(NoDuplo(1))
lista.adicionar_no(NoDuplo(2))
lista.adicionar_no(NoDuplo(3))
lista.adicionar_no(NoDuplo(4))
lista.adicionar_no(NoDuplo(5))
lista.adicionar_no(NoDuplo(6))
lista.adicionar_no(NoDuplo(7))
lista.adicionar_no(NoDuplo(8))
lista.adicionar_no(NoDuplo(9))
print(lista.imprimir_pela_cauda())
print(lista.imprimir_pela_cabeca())
print(lista.existe_valor(4))
lista.remover_valor(4)
print(lista.imprimir_pela_cabeca())
lista.remover_valor(1)
print(lista.imprimir_pela_cabeca())
lista.remover_valor(9)
print(lista.imprimir_pela_cabeca())
