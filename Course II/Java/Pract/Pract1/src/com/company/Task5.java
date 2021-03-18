package com.company;

public class Task5 {
    //Дано два числа a и b. Найдите гипотенузу треугольника с заданными катетами.
    public static int pow(int value) {
        return value * value;
    }

    public static void main(String[] args) {
        int a = 3;
        int b = 4;
        int c = pow(a) + pow(b);
        System.out.println("Результат: " + Math.sqrt(c));
    }
}
