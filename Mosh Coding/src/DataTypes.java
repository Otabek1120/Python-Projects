import java.util.Date;

public class DataTypes {
    public static void main(String[] args) {
        byte age = 30;
        long viewsCount = 3_123_456_789L;
        float price = 10.99F;
        char letter = 'A';
        boolean isEligible = false;

        // When creating a reference, we need to use new
        Date now = new Date();
        System.out.println(now);

        // References
        byte x = 1;
        byte y = x;
        x = 2;
        System.out.println(y);

        

    }
}