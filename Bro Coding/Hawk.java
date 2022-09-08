// INTERFACE 
// Super class
public class Hawk implements Predator{

    @Override
    public void hunt() {
        // TODO Auto-generated method stub
        System.out.println("The hawk is hunting");
    }

    @Override
    public void eat() {
        System.out.println("The hawk is eating a prey");
    }
    
}
