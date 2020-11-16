package com.task1;
/*Дано натуральное число n. Выведите все числа от 1 до n.*/

public class Recursion {
    public static void main(String[] args) {
        System.out.println(recursion(10)); // вызов рекурсивной функции
    }

    public static String recursion(int n) {
        // Базовый случай
        if (n == 1) {
            return "1";
        }
        // Шаг рекурсии / рекурсивное условие
        return recursion(n - 1) + " " + n;
    }

}

