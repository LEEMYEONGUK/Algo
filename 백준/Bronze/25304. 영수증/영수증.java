import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int X = sc.nextInt();
        int N = sc.nextInt();

        int sm = 0;

        for (int i = 0; i < N; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            sm += a * b;
        }

        if (X == sm) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}
