class Fila:
    def __init__(self):
        self.dados = []

    def enqueue(self, valor):
        self.dados.append(valor)

    def dequeue(self):
        return self.dados.pop(0)

    def is_empty(self):
        return not self.dados

    def inicio(self):
        return self.dados[0]

    def size(self):
        return len(self.dados)

    def __str__(self):
        return str(self.dados)
