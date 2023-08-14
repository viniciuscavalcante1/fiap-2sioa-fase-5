from utils.Nodo import Nodo
from utils.ListaEncadeadaSimples import ListaEncadeadaSimples

nodo = Nodo(1)
print(f"Nodo: {nodo}")
lista_simples = ListaEncadeadaSimples(nodo)
lista_simples.adicionarNodo(Nodo(2))
lista_simples.adicionarNodo(Nodo(3))
lista_simples.adicionarNodo(Nodo(4))
lista_simples.adicionarNodo(Nodo(5))
lista_simples.imprimirLista()
print(lista_simples)
print(lista_simples.valorExiste(0))