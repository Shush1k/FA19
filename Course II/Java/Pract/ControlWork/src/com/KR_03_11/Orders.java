package com.KR_03_11;

import java.util.ArrayList;

public class Orders {

    int tableID;
    double orderSum;
    ArrayList<Menu> orders = new ArrayList<>();

    public Orders(int tableID) {
        this.tableID = tableID;
    }

    public void add(String name) {
        if (Menu.menuHashMap.containsKey(name)) {
            if (Menu.menuHashMap.get(name).amount == 0) {
                Menu.stopList.put(name, Menu.menuHashMap.get(name));
                System.out.println("Sorry, but " + name + " is over.");
            } else {
                Menu.menuHashMap.get(name).setAmount(Menu.menuHashMap.get(name).amount - 1);
                setOrderSum(Menu.menuHashMap.get(name).price);
                orders.add(Menu.menuHashMap.get(name));
                System.out.println(name + " is successfully added to your order.");
            }
        } else
            System.out.println("Sorry, but " + name + " isn`t in menu.");
    }

    public void printOrders() {
        System.out.println("Table " + tableID);
        for (Menu value : orders) {
            System.out.println(value);
        }
    }
    public void done(String name, int count){
        if (Menu.menuHashMap.containsKey(name)){
            System.out.println("x"+count+" "+name + " already on Table.");
        }
    }

    public void done(String name){
        if (Menu.menuHashMap.containsKey(name)){
            System.out.println(name + " already on Table.");
        }
    }

    public void closeTable() {
        orders.clear();
        orderSum = 0;
        System.out.println("Table "+tableID+" is closed");
    }

    public void setOrderSum(double orderSum) {
        this.orderSum += orderSum;
    }

    public double getOrderSum() {
        return orderSum;
    }
    public void totalSum() {
        System.out.println("Table "+tableID+ " bill: $" +getOrderSum());
    }
}
