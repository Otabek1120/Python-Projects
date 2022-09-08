// MEHTOD OVERRIDING
// Sub class

public class Lion extends Animal{
    

    public Lion(String name) {
        super(name);
        //TODO Auto-generated constructor stub
    }

    @Override
    public void hunt() {
        System.out.println("The " + this.name + " hunts");
    }
}
