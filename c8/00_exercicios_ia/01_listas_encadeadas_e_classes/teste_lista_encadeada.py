from utils.No import No
from utils.ListaEncadeadaSimples import ListaEncadeadaSimples

lista = ListaEncadeadaSimples()
lista.adicionar_no(No(1))
lista.adicionar_no(No(2))
print(lista.imprimir_lista())
print(lista.procurar_cauda())
