
public class MathClass{
    public static void main(String[] args) {
        int result = Math.round(1.5F);
        System.out.println(result);
        System.out.println();
        
        // Math.ceil returns a dobule >= the given double
        int x = (int) Math.ceil(1.1F);
        System.out.println(x);
        // Math.floor returns a dobule <= the given double 
        int y = (int) Math.floor(1.1F);
        System.out.println(y);
        System.out.println();

        // Math.random --> ret
        double x2 = Math.random();
        System.out.println(x2);
        int x3 = (int) Math.round(Math.random() * 100);
        System.out.println(x3);
    }
}