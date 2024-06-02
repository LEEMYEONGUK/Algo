import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int sm = 0;
        for (int i = 1; i < n + 1; i++) {
            sm += i;
        }
        System.out.println(sm);
    }
}
