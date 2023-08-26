from utils.Nodo import Nodo
from utils.ListaDuplamenteEncadeada import ListaDuplamenteEncadeada

lista_dupla = ListaDuplamenteEncadeada()
lista_dupla.adicionar_nodo(Nodo(10))
lista_dupla.adicionar_nodo(Nodo(11))
lista_dupla.adicionar_nodo(Nodo(12))
lista_dupla.adicionar_nodo(Nodo(13))
lista_dupla.adicionar_nodo(Nodo(14))
lista_dupla.adicionar_nodo(Nodo(15))

lista_dupla.imprimir_pela_cabeca()
lista_dupla.imprimir_pela_cauda()
print(lista_dupla.existe_valor(10))