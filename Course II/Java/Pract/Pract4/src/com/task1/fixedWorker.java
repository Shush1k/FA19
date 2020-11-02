package com.task1;

public class fixedWorker extends worker {

    public fixedWorker(int id, String name, double salary){
        super(id, name, salary);
    }

    @Override
    public double calculateSalary() {
        return salary;
    }
}
