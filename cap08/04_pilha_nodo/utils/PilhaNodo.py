class PilhaNodo:
    def __init__(self):
        self.topo = None

    def empilhar(self, nodo):
        if self.topo is None:
            self.topo = nodo
        else:
            nodo.proximo = self.topo
            self.topo = nodo

    def desempilhar(self):
        nodo = self.topo
        self.topo = self.topo.proximo
        return nodo

    def e_vazia(self):
        if self.topo is None:
            return True
        return False

    def tamanho(self):
        tamanho = 0
        nodo = self.topo
        while nodo is not None:
            tamanho += 1
            nodo = nodo.proximo
        return tamanho

    def topo(self):
        if self.topo is not None:
            return self.topo.valor
        return None