// ABSTRACT keyword
// Subclass

public class Cars extends Vehicles{
    String name;

    public Cars(String name) {
        this.name = name;
    }
    @Override
    public void run() {
        // TODO Auto-generated method stub
        System.out.println("This " + this.name + 
                                " runs very well");
    }


}
