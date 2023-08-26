import java.util.*;

public class FILA_PROCESSOS {

    private static class NO{
        public  int dado;
        public  NO prox;
    }

    private static NO ini;
    private static NO fim;

    private static class Retorno{
        public  int item;
        public  boolean ok;
    }

    public void INIT() {
        ini = null;
        fim = null;
    }


    public boolean IsEmpty() {
        return (ini == null && fim == null);
    }

    public void ENQUEUE(int item) {
        NO novo = new NO();
        novo.dado = item;
        novo.prox = null;
        if (IsEmpty())
            ini = novo;
        else
            fim.prox = novo;
        fim = novo;
    }

    public Retorno DEQUEUE() {
        Retorno saida = new Retorno();
        if(!IsEmpty()) {
            saida.item = ini.dado;
            ini = ini.prox;
            if (ini == null) fim = null;
            saida.ok = true;
        }
        else
            saida.ok = false;
        return saida;
    }

    public Retorno FIRST() {
        Retorno saida = new Retorno();
        if(!IsEmpty()) {
            saida.item = ini.dado;
            saida.ok = true;
        }
        else
            saida.ok = false;
        return saida;
    }


    public static void main(String[] args) {
        // TODO Auto-generated method stub

        FILA_PROCESSOS fila = new FILA_PROCESSOS();
        Retorno resultado = new Retorno();
        Scanner entrada = new Scanner(System.in);

        int pid, op, resp;
        fila.INIT();
        do{
            System.out.println("1- inserir processo");
                    System.out.println("2- executar processo");
                            System.out.println("3- sair");
                                    op = entrada.nextInt();
            switch(op) {
                case 1:
                    System.out.println("pid: ");
                    pid = entrada.nextInt();;
                    fila.ENQUEUE(pid);
                    break;
                case 2:
                    resultado = fila.DEQUEUE();
                    if (resultado.ok) {
                        System.out.println("processo em execucao: "+ resultado.item);
                        System.out.println("processo foi concluido? (1-sim/2-não):");
                        resp = entrada.nextInt();
                        if (resp==2)
                            fila.ENQUEUE(resultado.item);
                        else
                            System.out.println("processo foi concluido" + resultado.item);
                    }
                    break;
                case 3:
                    System.out.println("fim da execucao");
                    /*esvaziar a fila*/
                    resultado = fila.DEQUEUE();
                    while (resultado.ok) {
                        System.out.println("processo finalizado: "+ resultado.item);
                        resultado = fila.DEQUEUE();
                    }
                    break;
                default:
                    System.out.println("opcao invalida");
            }
        }while(op !=3);
        entrada.close();
    }

}