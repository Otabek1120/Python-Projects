// CONSTRUCTORS

public class Human {
    private String name;
    private int age;
    private double weight;

    public Human(String name, int age, double weight) {
        this.name = name;
        this.age = age;
        this.weight = weight;
    }

    public void info() {
        System.out.println(this.name + " is " + 
        String.valueOf(this.age) + " years old and " +
        "weighs " + String.valueOf(this.weight) + " pounds.");
    }
}
