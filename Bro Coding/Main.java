public class Main {
    public static void main(String[] args) {
        // Car car = new Car();
        
        // System.out.println(car.model);
        // car.drive();
        // car.brake();

        // Human rick = new Human("Rick", 65, 130);
        // Human tony = new Human("Tony", 16, 100);
        // rick.info();
        // tony.info();

        /*
            OVERLOADED CONSTRUCTORS
        */
        // Pizza pizza1 = new Pizza("thick crust", 
        //                             "tomato", 
        //                             "mozzzerella", 
        //                             "mushroom");
        
        // Pizza pizza2 = new Pizza("thick crust", 
        //                             "tomato", 
        //                             "mozzzerella");
        
        // Pizza pizza3 = new Pizza("thick crust", 
        //                             "tomato");

        // System.out.println(pizza1.toString());
        // System.out.println(pizza2.toString());
        // System.out.println(pizza3.toString());

        /*
            STATIC keyword
        */
        // Friend friend1 = new Friend("Tim");
        // Friend friend2 = new Friend("Tony");
        // Friend friend3 = new Friend("Tom");
        // Friend friend4 = new Friend("Tiny");

        // System.out.println(Friend.numOfFriends);
        // System.out.println(friend1.numOfFriends);
        // Friend.display();

        /*
            INHERITANCE
        */

        // Car1 car = new Car1(200, 4, 2020);
        // Bicycle bicycle = new Bicycle(60, 2, 2019);

        // System.out.println(car.toString());
        // System.out.println();
        // System.out.println(bicycle.toString());

        // car.move();
        // car.stop();
        // bicycle.move();
        // bicycle.stop();

        /*
            METHOD OVERRIDING
        */
        // Animal animal = new Animal("tiger");
        // animal.hunt();
        // Lion lion = new Lion("lion");
        // lion.hunt();

        /*
          SUPER keyword 
        */
        // Hero hero = new Hero("Superman", 43, "Everything");
        // System.out.println(hero.toString());

        /*
          ABSTRACT keyword 
        */
        //Vehicles vehicle = new Vehicles(); throws an error
        // Cars car = new Cars("Prius, Toyota");
        // car.run();

        /*
           INTERFACE  
        */
        Rabbit rabbit = new Rabbit();
        Hawk hawk = new Hawk();
        Fish fish = new Fish();

        rabbit.flee();
        hawk.hunt();
        fish.flee();
        fish.hunt();

        

    }
    
}
