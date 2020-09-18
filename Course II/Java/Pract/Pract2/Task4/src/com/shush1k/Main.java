package com.shush1k;
/*Реализовать иерархию классов, описывающие трехмерные фигуры (Рисунок 1)
Класс Box является контейнером, он можем содержать в себе другие фигуры. Метод add()
принимает на вход Shape. Нужно добавлять новые фигуры до тех пор, пока для них
хватаем места в Box (будем считать только объём, игнорируя форму. Допустим, мы
переливаем жидкость). Если места для добавления новой фигуры не хватает, то метод
должен вернуть false.*/
public class Main {

    public static void main(String[] args) {

        // Коробка
        Box box = new Box();
        //Максимальный объём коробки
        box.setVolume(100);

        //Шар с объёмом 40
        Ball ball1 = new Ball();
        ball1.setVolume(40);


        System.out.println("\nОбъём коробки: " + box.getVolume());
        System.out.println("Объект добавили?: " + box.add(ball1));
        System.out.println("Объём коробки: " + box.getVolume());


        Pyramid pyramid = new Pyramid();
        pyramid.setVolume(10);
        System.out.println("\nОбъём коробки: " + box.getVolume());
        System.out.println("Объект добавили?: " + box.add(pyramid));
        System.out.println("Объём коробки: " + box.getVolume());

        Cylinder cylinder = new Cylinder();
        cylinder.setVolume(55);
        System.out.println("\nОбъём коробки: " + box.getVolume());
        System.out.println("Объект добавили?: " + box.add(cylinder));
        System.out.println("Объём коробки: " + box.getVolume());



    }
}
