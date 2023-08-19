from utils.Nodo import Nodo
from utils.Fila import Fila

fila = Fila()
fila.enfileirar(Nodo(1))
fila.enfileirar(Nodo(2))
fila.enfileirar(Nodo(3))

print(fila.desenfileirar())
print(fila.desenfileirar())
print(fila.desenfileirar())
