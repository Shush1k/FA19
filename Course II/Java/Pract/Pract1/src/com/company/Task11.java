package com.company;

public class Task11 {
    //Реализуйте метод, в который передается две целочисленные переменные и возвращает их среднее геометрическое
    public static void main(String[] args) {
        System.out.println(AvgGeom(3, 10));
    }

    public static double AvgGeom(double a, double b) {

        return Math.sqrt(a * b);
    }
}
