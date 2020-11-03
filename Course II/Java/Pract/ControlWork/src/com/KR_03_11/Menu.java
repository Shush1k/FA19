package com.KR_03_11;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;

public class Menu {
    // Характеристики
    String name;
    double price;
    int calories;
    double liter;
    int amount;
    HashSet<String> consistency;

    static HashMap<String, Menu> stopList = new HashMap<>();
    static ArrayList<Menu> menu = new ArrayList<>();
    static HashMap<String, Menu> menuHashMap = new HashMap<>();

    public void setName(String name) {
        this.name = name;
    }

    public void setCalories(int calories) {
        this.calories = calories;
    }

    public void setLiter(double liter) {
        this.liter = liter;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }

    public void setConsistency(HashSet<String> consistency) {
        this.consistency = consistency;
    }

    public static void addAmount(String name, int amount) {
        if (Menu.menuHashMap.containsKey(name)) {
            Menu.menuHashMap.get(name).setAmount(Menu.menuHashMap.get(name).amount + amount);
            Menu.stopList.remove(name);
        }
    }


    public static void print() {
        System.out.println("Menu:");
        for (Menu value : menu) {
            System.out.println(value);
        }
    }

    public static void printStopList() {
        System.out.println("StopList:");
        for (String value: stopList.keySet()) {
            System.out.println(stopList.get(value));
        }
    }
}