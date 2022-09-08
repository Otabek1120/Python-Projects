// OVERLOADED CONSTRUCTORS

public class Pizza {
    private String bread;
    private String sauce;
    private String cheese;
    private String topping;

    public Pizza(String bread, String sauce, String cheese, String topping) {
        this.bread = bread;
        this.sauce = sauce;
        this.cheese = cheese;
        this.topping = topping;
    }

    public Pizza(String bread, String sauce, String cheese) {
        this.bread = bread;
        this.sauce = sauce;
        this.cheese = cheese;
        this.topping = "no topping";
    }

    public Pizza(String bread, String sauce) {
        this.bread = bread;
        this.sauce = sauce;
        this.cheese = "no cheese";
        this.topping = "no topping";
    }

    public String toString() {
        String string = "This is a "+ this.bread
                                    + ", " + this.sauce
                                    + ", " + this.cheese
                                    + ", " + this.topping
                                    + " pizza";
        return string;

    }
    
}
