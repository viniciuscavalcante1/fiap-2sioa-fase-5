class Fila:
    def __init__(self):
        self.dados = []

    def __str__(self):
        return str(self.dados)

    def enfileirar(self, valor):
        self.dados.append(valor)

    def desenfileirar(self):
        return self.dados.pop(0)

    def e_vazia(self):
        return not self.dados

    def tamanho(self):
        return len(self.dados)

    def inicio(self):
        return self.dados[0]