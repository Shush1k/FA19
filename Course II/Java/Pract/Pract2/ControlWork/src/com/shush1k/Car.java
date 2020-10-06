package com.shush1k;

public class Car {
    protected String color;
    protected int maxSpeed;
    protected String gearboxType;
    protected int currSpeed;
    protected int price;
    protected String brand;
    protected int size = 1;



    Car(String color, int maxSpeed, String type, int currSpeed, int price, String brand) {
        this.color = color;
        this.maxSpeed = maxSpeed;
        this.gearboxType = type;
        this.currSpeed = currSpeed;
        this.price = price;
        this.brand = brand;
        this.size = size;
    }

    public int getSize() {
        return size;
    }

    public void setCurrSpeed(int currSpeed) {

        this.currSpeed = currSpeed;
    }

    public String getBrand() {
        return brand;
    }

    public int getCurrSpeed() {

        return currSpeed;
    }

    public void setMaxSpeed(int maxSpeed) {

        this.maxSpeed = maxSpeed;
    }

    public int getMaxSpeed() {

        return maxSpeed;
    }

    public void setGearboxType(String gearboxType) {
        this.gearboxType = gearboxType;
    }

    public String getGearboxType() {

        return gearboxType;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public int getPrice() {

        return price;
    }

    public void setColor(String color) {

        this.color = color;
    }

    public String getColor() {

        return color;
    }

    public void start(){
        while (this.currSpeed < this.maxSpeed){
            this.currSpeed++;
        }
        System.out.println("Старт:\n"+"Скорость машины = " + this.currSpeed+"\n");
    }

    public void stop(){
        if (this.currSpeed != 0){
            this.currSpeed = 0;
        } else {
            throw new ArithmeticException();
        }
        System.out.println("Стоп:\n"+"Скорость машины = " + this.currSpeed+"\n");
    }

    public void accelerate(int speed){
        // Изменение скорости машины
        if (this.currSpeed+speed < maxSpeed) {
            this.currSpeed += speed;
            System.out.println("Изменение скорости машины на "+speed+":\nТекущая скорость машины = " + this.currSpeed+"\n");
        }
        else {
            System.out.println("Изменение скорости машины:\n");
            System.out.println("Скорость машины не может превысить максимальную!\n"+"Текущая скорость = "+this.currSpeed);
        }
    }

    @Override
    public String toString() {
        return "Car: " +
                "color='" + color + '\'' +
                ", maxSpeed=" + maxSpeed +
                ", gearboxType='" + gearboxType + '\'' +
                ", currSpeed=" + currSpeed +
                ", price=" + price +
                ", brand='" + brand + '\'';
    }
}