class ListaEncadeadaSimples:
    def __init__(self, cabeca=None):
        self.cabeca = cabeca

    def adicionarNodo(self, nodo):
        if self.cabeca is None:
            self.cabeca = nodo
        else:
            cauda = self.procurarCauda(self.cabeca)
            cauda.proximo = nodo

    def procurarCauda(self, nodo):
        if nodo.proximo is None:
            return nodo
        return self.procurarCauda(nodo.proximo)

    def imprimirLista(self):
        nodo = self.cabeca
        while nodo is not None:
            print(nodo, end=' ')
            nodo = nodo.proximo

    def valorExiste(self, valor):
        nodo = self.cabeca
        while nodo is not None:
            if nodo.valor == valor:
                return 1
            else:
                nodo = nodo.proximo
        return 0

    def removerNodo(self, nodo_excluir):
        # Caso especial: a lista está vazia
        if self.cabeca is None:
            return

        # Caso especial: o nodo a ser excluído é o primeiro nodo da lista
        if self.cabeca == nodo_excluir:
            self.cabeca = self.cabeca.proximo
            return

        nodo_atual = self.cabeca
        nodo_anterior = None

        # Percorre a lista para encontrar o nodo a ser excluído
        while nodo_atual is not None and nodo_atual != nodo_excluir:
            nodo_anterior = nodo_atual
            nodo_atual = nodo_atual.proximo

        # Verifica se o nodo a ser excluído foi encontrado
        if nodo_atual is None:
            return

        # Atualiza as referências para remover o nodo da lista
        nodo_anterior.proximo = nodo_atual.proximo

