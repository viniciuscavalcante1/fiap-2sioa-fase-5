public class ex1 {
    public static double avalia(double x, int n) {
        if (x > 0) {
            return avalia(x - n, n + 1);
        } else {
            return x;
        }
    }

    public static void main(String[] args) {
        System.out.println(avalia(3.2, 1));
    }
}


