package com.shush1k;

public class Main {

    public static void main(String[] args){
        System.out.println("Спорткар 1:");
        SportCar sportCar_1 = new SportCar("Red", 320, "Auto", 180, 21500000, "Mclaren 720 s");
        sportCar_1.start();
        sportCar_1.accelerate(-10);
        sportCar_1.stop();

        Car car_1 = new Car("White", 160, "Auto", 90, 5600000,
                "Audi");

        System.out.println("Спорткар 2:");
        SportCar sportCar_2 = new SportCar("Black", 260, "Mech", 95, 2500000, "BMW");
        sportCar_2.start();
        sportCar_2.accelerate(-50);
        sportCar_2.stop();


        Garage garage = new Garage(3, 0);
        garage.addAuto(sportCar_1);
        garage.addAuto(car_1);
        garage.addAuto(sportCar_2);
        garage.addAuto(sportCar_2);
        System.out.println("Занято мест: "+garage.getSum()+" из "+garage.getMaxCap());
    }
}