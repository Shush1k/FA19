package com.company;

public class Task10 {
    // Реализуйте метод, в который передается две целочисленные переменные и возвращает их среднее арифметическое
    public static void main(String[] args) {
        System.out.println(AvgArm(3, 6)); // Выведет 4 если тип переменных int, если double то 4.5.
        System.out.println(AvgArm(-10,10));
        System.out.println(AvgArm(-10,30));

    }

    public static float AvgArm(float a, float b) {

        return (a + b) / 2;
    }
}