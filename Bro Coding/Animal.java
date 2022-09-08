// METHOD OVERRIDING 
// Parent class

public class Animal {
    String name;

    public Animal(String name) {
        this.name = name;
    }

    public void hunt() {
        System.out.println("The " + this.name +" hunts");
    }
}
