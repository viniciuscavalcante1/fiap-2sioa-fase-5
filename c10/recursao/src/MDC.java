import java.util.Scanner;

public class MDC {
    public static int mdc(int n, int m) {
        if (n > m) {
            return (mdc(m, n));
        } else {
            if (n == 0) {
                return (m);
            } else {
                return (mdc(n, m % n));
            }
        }
    }

    public static void main(String[] args) {
        Scanner entra = new Scanner(System.in);
        System.out.println("Digite 2 números inteiros: ");
        int n = entra.nextInt();
        int m = entra.nextInt();
        System.out.println("O MDC de " + n + " e " + m + " é " + mdc(n, m));
    }
}
