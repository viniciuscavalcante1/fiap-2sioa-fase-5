class Nodo:
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo

    def __str__(self):
        return str(self.valor)

    