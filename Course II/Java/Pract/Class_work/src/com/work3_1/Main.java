package com.work3_1;
// Интерфейсы - событийная модель, нужен для реализации метода в дальнейших классах
// StringBuilder
public class Main {
    public static void main(String[] args) {
        Print book = new Print("Ivan", "Ivanov");
        book.print();
        Printable.read();
        System.out.println("\n");
//
//
//
//        Button button = new Button(new ButtonClickHandler());
//        button.click();


    }
}



