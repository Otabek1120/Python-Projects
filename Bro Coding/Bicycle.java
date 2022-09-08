// INHERITANCE 
// Subclass

public class Bicycle extends Vehicle {
    private int pedals;

    public Bicycle (double speed, int wheels, int year) {
        this.speed = speed;
        this.wheels = wheels;
        this.year = year;
        this.pedals = 2;
    }

    public String toString() {
        String info = speed + "\n"
                        + wheels + "\n"
                        + year + "\n"
                        + pedals;
        return info;
    }
}
