import java.io.IOException;
import java.util.*;

public class PILHA_CHAR {

    /* Inicio da resposta */
    private static class NO {
        public char dado;
        public NO prox;
    }

    private static NO topo;

    public boolean IsEmpty() {
        return topo == null;
    }

    public void PUSH(char item) {
        NO novo = new NO();
        novo.dado = item;
        novo.prox = topo;
        topo = novo;
    }

    public char POP() {
        char item = topo.dado;
        topo = topo.prox;
        return item;
    }

    private void mostra() {
        // TODO Auto-generated method stub
        NO aux = topo;
        while (aux != null) {
            System.out.println(aux.dado);
            aux = aux.prox;
        }
    }
    /* Final da resposta */

    public static void main(String[] args) throws IOException {
        // TODO Auto-generated method stub

        PILHA_CHAR s = new PILHA_CHAR();


        Scanner entrada = new Scanner(System.in);
        char item;
        int j = 0;
        char comp[] = new char[10];
        System.out.println("Digite paralavra ");
        String nome = entrada.nextLine();

        for (int i = 0; i < nome.length(); i++) {
            item = nome.charAt(i);
            comp[j] = item;
            j++;
            s.PUSH(item);
        }

        s.mostra();


        boolean ok = true;
        j = 0;
        while (!s.IsEmpty() && ok) {
            item = s.POP();
            if (comp[j] != item) ok = false;
            j++;
        }
        if (ok)
            System.out.println("é palindromo");
        else
            System.out.println("NAO é palindromo");
        entrada.close();
    }


}