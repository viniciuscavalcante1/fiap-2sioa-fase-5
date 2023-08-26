class ListaDuplamenteEncadeada:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def adicionar_nodo(self, nodo):
        if self.cabeca is None and self.cauda is None:
            self.cabeca = nodo
            self.cauda = nodo
        elif self.cabeca.proximo is None:
            nodo.anterior = self.cabeca
            self.cabeca.proximo = nodo
            self.cauda = nodo
        else:
            self.cauda.proximo = nodo
            nodo.anterior = self.cauda
            self.cauda = nodo

    def imprimir_pela_cabeca(self):
        nodo = self.cabeca
        while nodo is not None:
            print(nodo, end=' ')
            nodo = nodo.proximo

    def imprimir_pela_cauda(self):
        nodo = self.cauda
        while nodo is not None:
            print(nodo, end=' ')
            nodo = nodo.anterior

    def existe_valor(self, valor):
        nodo = self.cabeca
        while nodo is not None:
            if nodo.valor == valor:
                return True
            else:
                nodo = nodo.proximo
        return False

    def remover_elemento(self, valor):
        nodo = self.cabeca
        while nodo is not None:
            if nodo.valor == valor:
                if valor == self.cabeca and valor == self.cauda:
                    self.cabeca = None
                    self.cauda = None
                elif valor == self.cabeca:
                    self.cabeca = nodo.proximo
                    self.cabeca.anterior = None
                elif valor == self.cauda:
                    self.cauda = nodo.anterior
                    self.cauda.proximo = None
                else:
                    nodo.anterior.proximo = nodo.proximo
                    nodo.proximo.anterior = nodo.anterior
                return
            nodo = nodo.proximo