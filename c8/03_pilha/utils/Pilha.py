class Pilha:
    def __init__(self):
        self.dados = []

    def __str__(self):
        return str(self.dados)

    def empilhar(self, valor):
        self.dados.append(valor)