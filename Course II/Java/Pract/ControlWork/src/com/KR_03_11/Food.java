package com.KR_03_11;

import java.util.HashSet;

public class Food extends Menu {
    public Food(String name, double price, int calories, int amount, HashSet<String> consistency) {
        this.name = name;
        this.price = price;
        this.calories = calories;
        this.amount = amount;
        this.consistency = consistency;
        menu.add(this);
        menuHashMap.put(name, this);

        if (amount == 0)
            stopList.put(name, this);
    }
    @Override
    public String toString() {
        return "{" +
                "\n\tName = " + name +
                "\n\tPrice = " + '$' +price +
                "\n\tCalories = " + calories +
                "\n\tAmount = " + amount +
                "\n\tConsistency = " + consistency +
                "\n}\n";
    }

}