
public class CompareOpers {
    public static void main(String[] args) {
        int temperature = 22;
        boolean isWarm = temperature > 20 && temperature < 30;
        System.out.println(isWarm);

        boolean hasHighIncome = true;
        boolean hasGoodCredit = true;
        boolean hasCrimeRecord = false;
        boolean isEligible =  (hasGoodCredit || hasHighIncome) && !hasCrimeRecord;
        System.out.println(isEligible);
    }
}