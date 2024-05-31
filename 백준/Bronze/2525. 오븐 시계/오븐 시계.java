import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int hour = sc.nextInt();
        int minute = sc.nextInt();
        int time = sc.nextInt();

        int afterMinute = minute + time;

        hour += afterMinute / 60;
        minute = afterMinute % 60;

        if (hour >= 24) {
            hour -= 24;
        }

        System.out.print(hour);
        System.out.print(" ");
        System.out.println(minute);
    }
}
