package com.shush1k;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        //Первая задача
        System.out.println("Первая задача");
        //Вызов через статический метод
        Main.buildDict("аывоыоаоыфарыфаоыфдвдцц");
        //Вторая задача
        System.out.println("Вторая задача");
        ArrayList<Integer> intList = new ArrayList<>();
        ArrayList<Character> charList = new ArrayList<>();
        for (int i=0; i<10; i++){
            intList.add(i);
        }
        System.out.println(intList.size());
        ArrayList<Integer> intList2 = new ArrayList<>();
        for (int i=0; i<15; i++){
            intList.add(i);
        }
        ArrayList<Integer> intList3 = new ArrayList<>();
        intList3.addAll(intList);
        intList3.addAll(intList2);
        System.out.println(intList3.size());
        Collection<Integer> coll = Main.removeDuplications(intList);
        System.out.println(coll.size());
    }
    public static void buildDict(String text){
        /** метод к первой задаче*/
        text = text.toLowerCase();
        int[] result = new int['я' - 'а'+1];
        for(int i=0; i<text.length(); i++){
            char ch = text.charAt(i);
            if(ch >= 'a' && ch <= 'я'){
                result[ch -'а']++;
            }

        }
        for(int i=0; i<result.length; i++){
            System.out.println((char)(i+'а')+" = "+ result[i]);
        }
    }


    public static <T>Collection<T> removeDuplications(Collection<T> coll){
        /** Метод ко второй задаче*/
        return new HashSet<>(coll);
    }
}
