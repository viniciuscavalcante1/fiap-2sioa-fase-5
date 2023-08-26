public class ex2 {
    public static int metodo(double vet[], int n, int c) {
        if (n >= 0) {
            if (vet[n] > 0) {
                return (metodo(vet, n - 1, c + 1));
            }
            else {
                return (metodo(vet, n - 1, c));
            }
        }
        else {
            return c;
        }
    }

    public static void main(String[] args) {
        double vet[] = {2.3, -4.7, 8.5, -6.6, -1.8};
        System.out.println(metodo(vet, 4, 0));
    }
}
