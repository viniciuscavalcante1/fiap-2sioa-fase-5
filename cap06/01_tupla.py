import sys

nome = "Vini, Cavalcante"
print(sys.getsizeof(nome))

nome_lista = ["Vini", "Cavalcante"]
print(sys.getsizeof(nome_lista))

nome_tupla = ("Vini", "Cavalcante")
print(sys.getsizeof(nome_tupla))

categorias = ("padawan", "knight", "master")
print(categorias)
print(categorias[1])
print(categorias[-1])

# desempacotamento
teste1, teste2, teste3 = categorias

for categoria in categorias:
    print(categoria)