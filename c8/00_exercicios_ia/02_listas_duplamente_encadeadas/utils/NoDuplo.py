class NoDuplo:
    def __init__(self, valor, proximo=None, anterior=None):
        self.valor = valor
        self.proximo = proximo
        self.anterior = anterior

    def __str__(self):
        return str(self.valor)
    