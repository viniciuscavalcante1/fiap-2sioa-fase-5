public class Main {
    public static void main(String[] args) {
        No lista = null;

        for(int i = 1; i <= 2; i++) {
            No novo = new No();
            novo.dado = i + 4;
            novo.prox = lista;
            lista = novo;
        }

        No aux = lista;
        while (aux != null) {
            System.out.println("Dado do nó apontado por prox: " + aux.dado);
            aux = aux.prox;
        }
    }
}