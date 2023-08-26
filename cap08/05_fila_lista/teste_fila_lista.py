from utils.Fila import Fila

fila = Fila()
fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)
print(f"fila: {fila}")

print(fila.desenfileirar())
print(f"fila: {fila}")
print(fila.desenfileirar())
print(f"fila: {fila}")
print(fila.desenfileirar())
