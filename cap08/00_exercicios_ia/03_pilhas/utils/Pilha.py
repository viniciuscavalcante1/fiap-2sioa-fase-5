class Pilha:
    def __init__(self):
        self.dados = []

    def push(self, valor):
        self.dados.append(valor)

    def pop(self):
        self.dados.pop()
        return

    def is_empty(self):
        return not self.dados

    def get_topo(self):
        return self.dados[-1]

    def size(self):
        return len(self.dados)

    def __str__(self):
        return str(self.dados)