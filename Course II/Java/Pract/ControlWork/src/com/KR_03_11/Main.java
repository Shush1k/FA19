package com.KR_03_11;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
/*
Реализовать операционную систему кафе.
Система должна позволять создать меню/изменять меню/добавлять блюда в стоп лист (блюда которые присутствуют в меню, но отсутствуют сегодня по какой-то причине)/отмечать какие блюда поданы/отображать информацию о заказе по столику/закрывать заказ
Система оформляет заказ по столам, выбивает итоговую сумму заказа
Система позволяет вбивать блюда как по кухне, так и по бару
У каждого проданного товара есть характеристики: цена за штуку товара, единица измерения, количество в единице измерения, состав
*/

public class Main {
    public static void main(String[] args) {
        // Создание меню
        Food f1 = new Food("Burger", 5, 300,3, new HashSet<>(Arrays.asList("Meat", "Bread", "Sauce", "Ketchup", "Salt")));
        Food f2 = new Food("Fries", 2.50, 100,4, new HashSet<>(Arrays.asList("Potato", "Salt")));
        Food f3 = new Food("Nuggets", 3, 150,6, new HashSet<>(Arrays.asList("Chicken", "Breading")));
        Food f4 = new Food("Salad Caesar", 6, 250, 5, new HashSet<>(Arrays.asList("Chicken", "Bread", "Caesar sauce", "Bacon", "Tomatoes")));
        Drinks d1 = new Drinks("Orange Juice", 4, 0.5, 10, new HashSet<>(Collections.singletonList("Orange Juice")));
        Drinks d2 = new Drinks("Apple Juice", 7, 1,0, new HashSet<>(Collections.singletonList("Apple Juice")));
        Drinks d3 = new Drinks("Bon Aqua", 8, 1,10, new HashSet<>(Collections.singletonList("Bon Aqua with minerals")));

//        Menu.print();
        /*t1, t2 .. tn - tables*/
        System.out.println("------------------------------------------------");
        Orders t1 = new Orders(1);
        System.out.println("Table 1");
        t1.add("Fries");
        t1.add("Cola");
        t1.add("Fries");
        t1.add("Fries");
        t1.printOrders();

        t1.done("Fries", 3);

        System.out.println("------------------------------------------------");
        Orders t2 = new Orders(2);
        System.out.println("Table 2");
        t2.add("Nuggets");
        t2.add("Fries");
        t2.add("Fries");
        t2.add("Bon Aqua");
        t2.add("Apple Juice");

        t2.done("Nuggets");
        System.out.println("------------------------------------------------");

        t1.totalSum();
        t1.closeTable();

        System.out.println("------------------------------------------------");

        t2.totalSum();
        t2.closeTable();

        System.out.println("------------------------------------------------");

        Menu.printStopList();
        System.out.println("------------------------------------------------");
        Menu.addAmount("Fries", 5);
        Menu.addAmount("Apple Juice", 2);
        f1.setConsistency(new HashSet<>(Arrays.asList("Meat", "Bread", "Sauce", "Salt", "Mustard")));
        f2.setPrice(1.99);

        Menu.print();
        System.out.println("------------------------------------------------");

    }

}
