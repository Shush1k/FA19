package com.task3;
/*Найдите корень уравнения cos x5 + x4-345.3*x-23=0 на отрезке [0;10] с точностью по x не хуже 0.001.
Известно, что на этом промежутке корень единственный. Используйте для этого метод деления отрезка пополам (и рекурсию).
*/
public class Equation {
    public static void main(String[] args) {
        System.out.println(halfDiv(0, 10));
    }
    public static double halfDiv(double start, double end){
        if(end - start <= 0.0001){
            return start;
        }

        double x = start + (end - start) / 2;

        if(equation(start) * equation(x) > 0){
            return halfDiv(x, end);
        } else {
            return halfDiv(start, x);
        }
    }
    public static double equation(double x){
        return Math.pow(x, 2) + 2*x - 16;
    }
}
