
public class CastingInJava {
    public static void main(String[] args) {
        // implicit casting --> happens when the data is not lost
        // byte > short > int > long > float > doubble
        short x = 1;
        int y = x + 2; // x is coverted to an int, or casted
        System.out.println(y);
        System.out.println();

        double m = 1.1;
        double n = m + 2; // here 2 becomes 2.00000...
        System.out.println(n);
        System.out.println();

        // explicit casting
        double h = 1.1;
        int i = (int) h + 2; // h becomes 1
        System.out.println(i);
        System.out.println();

        // string to int
        String x1 = "1";
        int y1 = Integer.parseInt(x1) + 2;
        System.out.println(y1);


    }
}