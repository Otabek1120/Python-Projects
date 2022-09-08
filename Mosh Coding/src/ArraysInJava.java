import java.util.Arrays;

public class ArraysInJava {
    public static void main(String[] args) {
        int [] numbers = new int[5];
        numbers[0] = 1;
        numbers[1] = 2;
        System.out.println(numbers); // it prints out the address
        System.out.println(Arrays.toString(numbers));

        // Another way of creating an array

        int [] nums = { 4, 2, 3, 1, 5};
        System.out.println(Arrays.toString(nums));
        System.out.println(nums.length);
        // once you create an array, you cant change the size
        Arrays.sort(nums);
        System.out.println(Arrays.toString(nums));
    }
}