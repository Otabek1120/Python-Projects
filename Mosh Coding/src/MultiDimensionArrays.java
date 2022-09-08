import java.util.Arrays;

public class MultiDimensionArrays {
    public static void main(String[] args) {
        int [][] numbers = new int [2][3]; // it has 2 rows and 3 columns
        numbers[0][0] = 10;
        numbers[1][0] = 20;
        System.out.println(Arrays.deepToString(numbers)); // have to use deepToString to print
                                                          // the vals of 2d arrays
        // 3d arrays
        int [][][] threeDNumbers = new int [2][2][2];
        System.out.println(Arrays.deepToString(threeDNumbers));

        //  { } usage to create arrays
        int [][] number2 = { { 1, 2, 3}, { 4, 5, 6 } };
        System.out.println(Arrays.deepToString(number2));
    }
}