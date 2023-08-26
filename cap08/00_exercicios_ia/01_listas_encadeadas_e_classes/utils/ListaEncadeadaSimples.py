class ListaEncadeadaSimples:
    def __init__(self, cabeca=None):
        self.cabeca = cabeca

    def adicionar_no(self, valor):
        if self.cabeca is None:
            self.cabeca = valor
        else:
            cauda = self.procurar_cauda()
            cauda.proximo = valor

    def procurar_cauda(self):
        no = self.cabeca
        if self.cabeca is None:
            return None
        while no.proximo is not None:
            no = no.proximo
        return no

    def imprimir_lista(self):
        no = self.cabeca
        if self.cabeca is None:
            return ''
        while no is not None:
            print(no.valor)
            no = no.proximo

    def remover_elemento(self, valor):
        if self.cabeca is None:
            return  # Lista vazia, não há nada para remover

        if self.cabeca.valor == valor:
            self.cabeca = self.cabeca.proximo
            return  # Removido o elemento da cabeça

        atual = self.cabeca
        while atual.proximo is not None and atual.proximo.valor != valor:
            atual = atual.proximo

        if atual.proximo is None:
            return  # Elemento não encontrado na lista

        atual.proximo = atual.proximo.proximo
