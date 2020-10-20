package com.shush1k;

import java.util.HashMap;
import java.util.Map;

public class Garage{
    int maxCap = 10;
    int currAuto;
    int sum;
    Map<String,Integer> dictionary = new HashMap<String,Integer>();

    Garage(int maxCap, int currAuto){
        this.maxCap = maxCap;
        this.currAuto = currAuto;
    }

    public void addAuto(Car car){
        this.sum = 0;
        for (int num : dictionary.values()){
            this.sum = this.sum + num;
        }
        if (!(this.sum + car.getSize() <= this.maxCap)){
            System.out.println("Гараж заполнен!Нет места!");

        // Нужно добавить в словарь машины
        }

    }
    public int getSum(){

        return sum;
    }
    public int getMaxCap(){

        return maxCap;
    }
}