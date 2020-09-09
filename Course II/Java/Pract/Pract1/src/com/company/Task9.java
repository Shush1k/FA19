package com.company;

public class Task9 {
    //Реализуйте метод, который получает целое число на вход и возвращает разницу между данным числом и 21
    //Выведите значения на экран с различными целыми числами
    public static void main(String[] args) {
        System.out.println(run(11));
        System.out.println(run(31));
        System.out.println(run(158));
    }
    public static int run(int numb){
        return numb-21;
    }
}
