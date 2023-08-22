import java.util.Scanner;

public class Fatorial {
    public static int fat(int n) {
        if (n == 0) {
            return 1;
        }
        else {
            return n * fat(n - 1);
        }
    }

    public static void main(String[] args) {
        int fat = 1;
        int n = 40;
        for (int i = n; i > 1; i--) {
            fat = fat * i;
        }

        Scanner entra = new Scanner(System.in);
        System.out.println("Digite um número: ");
        int num = entra.nextInt();
        System.out.println("O fatorial de " + num + " é " + fat(num));
    }
}