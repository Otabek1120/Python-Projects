import java.util.Scanner;

public class ReadingInput {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Age: ");
        byte age = scanner.nextByte();
        System.out.println("You are " + age);
        System.out.println();

        // differences Scanner.next() vs Scanner.nextline()
        //  Scanner.next retruns the next first token
        Scanner scanner2 = new Scanner(System.in);
        System.out.print("Name: ");
        String name = scanner2.next();
        System.out.println("You are " + name);
        // Scanner.nextLine() return the next line
        Scanner scanner3 = new Scanner(System.in);
        System.out.print("Name: ");
        String name2 = scanner3.nextLine().trim();
        System.out.println("You are " + name2);

    }
}