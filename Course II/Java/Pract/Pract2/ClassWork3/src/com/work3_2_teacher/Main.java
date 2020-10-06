package com.work3_2_teacher;

public class Main {
    public static void main(String[] args) {
        BaseConverter baseConverter = new BaseConverter(10);
        // Как это должно работать? Убрал boolean тип и возвращаю baseValue в методе setBase
        System.out.println(baseConverter.setBase('F'));
        System.out.println(baseConverter.setBase('K'));
        System.out.println(baseConverter.setBase('F'));
        System.out.println(baseConverter.setBase('C'));
    }
}
