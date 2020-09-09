package com.company;

public class Task12 {
    //Реализуйте метод, в который передается 4 числа с плавающей точкой.
    //Первые два числа – координаты x, y первой точки. Вторые два числа – координаты x,y второй точки. Найти расстояние между двумя точками
    public static void main(String[] args) {
        System.out.println("Растояние между точками: "+Range(2.0, 3.3, 4.4, 2.1));
    }
    public static double Range(double x1, double x2, double y1, double y2){
        return Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
    }
}
