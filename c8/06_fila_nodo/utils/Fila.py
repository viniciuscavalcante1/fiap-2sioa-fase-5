class Fila:
    def __init__(self):
        self.inicio = None

    def enfileirar(self, nodo):
        if self.inicio is None:
            self.inicio = nodo
        elif self.inicio.proximo is None:
            self.inicio.proximo = nodo
        else:
            fim = self.encontrar_fim()
            fim.proximo = nodo

    def encontrar_fim(self):
        nodo = self.inicio
        while nodo.proximo is not None:
            nodo = nodo.proximo
        return nodo

    def desenfileirar(self):
        nodo = self.inicio
        self.inicio = nodo.proximo
        return nodo

