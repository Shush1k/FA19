package com.task1;


public class hourWorker extends worker {


    public hourWorker(int id, String name, double per_hour){
        super(id, name,per_hour);
    }

    @Override
    public double calculateSalary() {
        return 20.8*8*this.salary;
    }
}
