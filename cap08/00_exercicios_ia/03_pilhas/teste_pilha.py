from utils.Pilha import Pilha

pilha = Pilha()
pilha.push(1)
pilha.push(2)
pilha.push(3)
pilha.push(4)
pilha.push(5)
print(pilha)

pilha.pop()
pilha.pop()
print(pilha)

print(pilha.is_empty())

print(pilha.get_topo())

pilha.pop()
pilha.pop()
pilha.pop()

print(pilha)
print(pilha.is_empty())
