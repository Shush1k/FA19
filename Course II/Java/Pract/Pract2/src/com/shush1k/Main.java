package com.shush1k;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	// Ввод строк с клавиатуры
        Scanner inp = new Scanner(System.in);
        String a = inp.next();
        String b = inp.next();
        System.out.println(func(a, b));
    }
    private static String func(String a, String b){
        return a+" "+b;
    }
}
