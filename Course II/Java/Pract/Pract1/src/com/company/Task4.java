package com.company;

public class Task4 {
    //Даны две переменные. Поменяйте значения переменных друг с другом двумя способами
    public static void main(String[] args) {
    int a = 5;
    int b = 15;
    System.out.println("Изначально: "+"\na = "+a+";\nb = "+b);
    int d = a;
    a = b;
    b = d;
    System.out.println("Результат 1: "+"\na = "+a+";\nb = "+b);
    //Математически
    a += b;
    b = a - b;
    a -= b;
    System.out.println("Результат 2: "+"\na = "+a);
    System.out.println("b = "+b);
    }
}
