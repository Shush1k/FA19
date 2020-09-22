package com.shush1k;
import java.util.*;

public class Main {

    public static void main(String[] args) {
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

    public static <T>Collection<T> removeDuplications(Collection<T> coll){
        return new HashSet<>(coll);
    }
}
