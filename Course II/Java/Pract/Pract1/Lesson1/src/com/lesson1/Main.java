package com.lesson1;

public class Main {
    public static void main(String[] args) {
        Car car = new Car("yellow", 270, "X6");
        System.out.println(car.getModel());
        System.out.println(car.speedInMiles());
        System.out.println(car.speedInMiles(true));
    }
}
