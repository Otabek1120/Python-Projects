// PRINTF

public class Printf {
    public static void main(String[] args) {
        // [conversion - character]
        boolean myBoolean = true;
        char myChar = '@';
        String mytString = "Me";
        int myInt = 50;
        double myDouble = 123456789.0;

       System.out.printf("%b\n", myBoolean); 
       System.out.printf("%c\n", myChar); 
       System.out.printf("%s\n", mytString); 
       System.out.printf("%d\n", myInt); 
       System.out.printf("%f\n", myDouble); 

       //[width]
       System.out.printf("Hello %10s\n", mytString); // right-justify
       System.out.printf("Hello %-10s\n", mytString); // - : left justify

       //[precision]: only for floats and doubles
       System.out.printf("%.3f\n", myDouble);
       System.out.printf("%,.3f\n", myDouble);

    }
}
