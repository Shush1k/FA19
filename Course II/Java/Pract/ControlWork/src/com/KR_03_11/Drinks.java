package com.KR_03_11;

import java.util.HashSet;

public class Drinks extends Menu {
    public Drinks(String name, double price, double liter, int amount, HashSet<String> consistency) {
        this.name = name;
        this.price = price;
        this.liter = liter;
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
                "\n\tLiter = " + liter +
                "\n\tAmount = " + amount +
                "\n\tConsistency = " + consistency +
                "\n}\n";
    }
}
