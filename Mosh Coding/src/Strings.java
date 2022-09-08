
public class Strings {
    public static void main(String[] args) {
        // Strings are not primitive but we can define them as one
        String message = "  Hello, world" + "!!  ";
        System.out.println(message);
        System.out.println(message.startsWith("!!"));
        System.out.println(message.length());
        System.out.println(message.indexOf("e"));
        System.out.println(message.indexOf("elm"));
        System.out.println(message.replace("!", "*"));

        // As strs are immutable replacement doesn't change
        // the original str
        System.out.println(message);

        System.out.println(message.toLowerCase());
        System.out.println(message.toUpperCase());
        System.out.println(message.trim());
        
    }
}