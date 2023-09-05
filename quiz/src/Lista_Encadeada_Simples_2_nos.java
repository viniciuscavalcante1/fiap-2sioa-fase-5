public class Lista_Encadeada_Simples_2_nos {
    public static class NO {
        public int dado;
        public NO prox;
    }

    public static void main(String[] args) {
        NO lista = null;
        System.out.println("Valor ponteiro lista: " + lista);
        for (int i = 2; i <= 3; i++) {
            NO novo = new NO();
            novo.dado = i + 5;
            novo.prox = lista;
            lista = novo;
        }
        System.out.println("Dado do NO apontado por lista: " + lista.dado);
        System.out.println("Dado do NO apontado por prox: " + lista.prox.dado);
    }
}