// STATIC keyword
// -> there is only one copy of the variable 
// and all instances of the class share it

public class Friend {
    String name;
    static int numOfFriends;

    public Friend(String name) {
        this.name = name;
        numOfFriends ++;
    }

    public static void display() {
        System.out.println("You have " + 
                            numOfFriends + " friends");
    }
    
}
