import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

//        System.out.println(a);
//        System.out.println(b);

//        if (a > b) {
//            System.out.println(">");
//        } else if (a < b) {
//            System.out.println("<");
//        } else {
//            System.out.println("==");
//        }

        System.out.println((a>b) ? ">" : (a<b) ? "<" : "==" );

    }
}
