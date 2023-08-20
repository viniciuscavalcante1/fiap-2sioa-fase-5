class ListaDuplamenteEncadeada:
    def __init__(self, cabeca=None, cauda=None):
        self.cabeca = cabeca
        self.cauda = cauda

    def adicionar_no(self, no):
        cabeca = self.cabeca
        if cabeca is None:
            self.cabeca = no
            self.cauda = no
            no.proximo = None
            no.anterior = None
            return
        if cabeca.proximo is None:
            self.cabeca.proximo = no
            self.cauda = no
            no.anterior = cabeca
            no.proximo = None
            return
        else:
            self.cauda.proximo = no
            no.anterior = self.cauda
            self.cauda = no
            no.proximo = None
            return

    def imprimir_pela_cabeca(self):
        no = self.cabeca
        while no is not None:
            print(no.valor)
            no = no.proximo

    def imprimir_pela_cauda(self):
        no = self.cauda
        while no is not None:
            print(no.valor)
            no = no.anterior

    def existe_valor(self, valor):
        no = self.cabeca
        while no is not None:
            if no.valor == valor:
                return True
            no = no.proximo
        return False

    def remover_valor(self, valor):
        no = self.cabeca
        if self.cabeca is None:
            return
        if self.cabeca.valor == valor and self.cabeca.proximo is None:
            self.cabeca = None
            self.cauda = None
            return
        if self.cabeca.valor == valor and self.cabeca.proximo is not None:
            self.cabeca = self.cabeca.proximo
            self.cabeca.anterior = None
            return
        if self.cauda.valor == valor:
            self.cauda.anterior.proximo = None
            self.cauda = self.cauda.anterior
            self.cauda.proximo = None
            return
        else:
            while no is not None:
                if no.valor == valor:
                    no.anterior.proximo = no.proximo
                    no.proximo.anterior = no.anterior
                    return
                no = no.proximo
