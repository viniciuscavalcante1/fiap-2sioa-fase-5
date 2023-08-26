class Pilha:
    def __init__(self):
        self.dados = []

    def __str__(self):
        return str(self.dados)

    def empilhar(self, valor):
        self.dados.append(valor)

    def desempilhar(self):
        return self.dados.pop()

    def eVazia(self):
        return not self.dados

    def tamanho(self):
        return len(self.dados)

    def topo(self):
        return self.dados[len(self.dados) - 1]