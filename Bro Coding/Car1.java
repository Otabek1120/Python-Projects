// INHERITANCE 
// Subclass

public class Car1 extends Vehicle{
    private int doors;
    
    public Car1 (double speed, int wheels, int year) {
        this.speed = speed;
        this.wheels = wheels;
        this.year = year;
        this.doors = 4;
    }

    public String toString() {
        String info = speed + "\n"
                        + wheels + "\n"
                        + year + "\n"
                        + doors;
        return info;
    }
}
