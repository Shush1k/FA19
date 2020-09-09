package com.lesson1;

public class Car {
    //private - Идентификатор доступа, атрибуты не доступны вне объекта
    private String color;
    private int speed;
    private String model;

    public Car(String color, int speed, String model){
        this.color = color;
        this.speed = speed;
        this.model = model;
    }

    public String getModel(){
        return model;
    }
    //void указывает, что данный метод ничего не возвращает
    public void setModel(String val){
        model = val;
    }
    // double - числа с плавающей точкой
    public double speedInMiles(){
        return speed*0.85;
    }
    public String speedInMiles(boolean condition){
        return String.valueOf(speed*0.85)+" Миль в час";
    }
    public static String hello(){
        return "Hello";
    }
}

