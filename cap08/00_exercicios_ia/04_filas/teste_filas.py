from utils.Fila import Fila

fila = Fila()
fila.enqueue(1)
fila.enqueue(2)
fila.enqueue(3)
fila.enqueue(4)
print(fila)
fila.dequeue()
print(fila)
print(fila.is_empty())
print(fila.inicio())