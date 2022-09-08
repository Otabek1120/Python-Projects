//INTERFACE

public class Fish implements Prey, Predator {

    @Override
    public void hunt() {
        // TODO Auto-generated method stub
        System.out.println("The fish is hunting a smaller fish");
        
    }

    @Override
    public void flee() {
        // TODO Auto-generated method stub
        System.out.println("The fish is fleeing from a bigger fish");
    }

    @Override
    public void eat() {
        System.out.println("The fish is eating smth");
    }
    
}
