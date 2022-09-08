
public class ArExprs {
    public static void main(String[] args) {
        double result = 10 / (double) 3;
        System.out.println(result);

        // incrementation
        int x = 1;
        x ++; 
        x += 1; // = x + 1
        // x = x / 2 --> x /= 2
        System.out.println(x);

        int y = 1;
        int z = y++; // post-fix increments only y, not z
        System.out.println(y);
        System.out.println(z);
        System.out.println();

        int y1 = 1;
        int z1 = ++y1; // pre-fix increments only y, not z
        System.out.println(y1);
        System.out.println(z1);


    }
}