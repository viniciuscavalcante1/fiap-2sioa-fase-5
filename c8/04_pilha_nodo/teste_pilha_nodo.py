from utils.Nodo import Nodo
from utils.PilhaNodo import PilhaNodo

pilha = PilhaNodo()

pilha.empilhar(Nodo(1))
pilha.empilhar(Nodo(2))
pilha.empilhar(Nodo(3))

print(pilha.desempilhar())
print(pilha.desempilhar())
print(pilha.desempilhar())


