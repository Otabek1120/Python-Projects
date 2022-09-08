import java.text.NumberFormat;

public class FormatNums{
    public static void main(String[] args) {
        // formatting currency
        NumberFormat currency = NumberFormat.getCurrencyInstance();
        String result = currency.format(1234567.890);
        System.out.println(result);
        System.out.println();

        // formatting percentage
        NumberFormat percent = NumberFormat.getPercentInstance();
        String result2 = percent.format(0.890);
        System.out.println(result2);

        String result3 = NumberFormat.getPercentInstance().format(0.89);
        System.out.println(result3);

    }
}