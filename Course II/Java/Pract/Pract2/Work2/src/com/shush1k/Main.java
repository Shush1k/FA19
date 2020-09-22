package com.shush1k;
import java.util.*;
/*
1)Реализовать метод, который принимает коллекцию и возвращает коллекцию без вопросов
2) Постройте частотный словарь букв алфавита. На вход метод принимает строку.
*/
public class Main {

    public static void main(String[] args) {
        //Первая задача
        System.out.println("Первая задача");
        //Вызов через статический метод
        Main.buildDict("аывоыоаоыфарыфаоыфдвдцциклмно");
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
        /* метод к первой задаче*/
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

    public static void buildDictWithMap(String text){
        text = text.toLowerCase();
        //словарь map
        Map<Character, Integer> map = new HashMap<>();

        for(int i=0; i<text.length(); i++){
            char ch = text.charAt(i);
            // Проверка на русские буквы
            if((ch>= 'а' && ch <= 'я' ) || ch == 'ё'){
                // передаем ch(символ) получаем пару ключ значение; compute - присвоение значения. lambda
                map.compute(ch, ((character, integer) -> integer == null ? 1: integer +1));
            }
        }
        //Набор элементов коллекции(Map.Entry) .entrySet - возвращает множество пар ключ значение
        ArrayList<Map.Entry<Character, Integer>> entries = new ArrayList<>(map.entrySet());
        // o1, o2 - объекты. compare сравнивание двух символов(ключей объектов)
        entries.sort(((o1, o2) -> Character.compare(o1.getKey(), o2.getKey())));
        for (Map.Entry<Character, Integer>enter : entries){
            System.out.println(enter.getKey()+" = "+ enter.getValue());
        }
    }
    public static <K, V> Map<V, Collection<K>> revertMap(Map<? extends K, ? extends V> map) {
        Map<V, Collection<K>> resultMap = new HashMap<>();

        Set<K> keys = (Set<K>) map.keySet();
        for(K key:keys){
            //получаем значение из словаря map по ключу
            V value = map.get(key);
            //функция
            resultMap.compute(value, (v, ks) ->{
                if (ks == null){
                    //создаем множество, если ничего нет
                    ks = new HashSet<>();
                }
                ks.add(key);
                return ks;
            });
        }
        return resultMap;
    }
    public static <T>Collection<T> removeDuplications(Collection<T> coll){
        /* Метод ко второй задаче*/
        return new HashSet<>(coll);
    }
}
