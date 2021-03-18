package com.company;

public class Task7 {
    //Дано неотрицательное целое число. Найдите число десятков в его десятичной записи (то есть вторую справа цифру его десятичной записи).
    public static void main(String[] args) {
        int x = 1321023;
        if (x > 0)
            System.out.println(x % 100 / 10);
        else
            System.out.println("Отрицательное число");
    }
}
