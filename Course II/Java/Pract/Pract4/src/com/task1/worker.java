package com.task1;


public  abstract class worker{

    private final int id;
    private final String name;
    double salary;

    public worker(int id, String name,double salary){
        this.id = id;
        this.name = name;
        this.salary = salary;
    }

    public int getId() {
        return id;
    }
    public String getName() {
        return name;
    }
    public double getSalary(){
        return salary;
    }
    public abstract  double calculateSalary();
}