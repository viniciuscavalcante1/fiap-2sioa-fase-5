from utils.Pilha_list import Pilha

pilha = Pilha()
print(f"pilha.eVazia(): {pilha.eVazia()}")
print(f"pilha.tamanho(): {pilha.tamanho()}")

pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)
pilha.empilhar(4)
pilha.empilhar(5)

print("Empilhando 1 - 5...")
print(f"pilha.eVazia(): {pilha.eVazia()}")
print(f"pilha.tamanho(): {pilha.tamanho()}")
print(f"pilha: {pilha}")

print("Desempilhando...")
print(f"pilha.desempilhar(): {pilha.desempilhar()}")
print(f"pilha: {pilha}")
print(f"pilha.topo(): {pilha.topo()}")
print(f"pilha.desempilhar(): {pilha.desempilhar()}")
print(f"pilha.desempilhar(): {pilha.desempilhar()}")
print(f"pilha.desempilhar(): {pilha.desempilhar()}")
print(f"pilha.desempilhar(): {pilha.desempilhar()}")
print(f"pilha: {pilha}")
print(f"pilha.eVazia(): {pilha.eVazia()}")