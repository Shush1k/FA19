package com.task2;

import java.util.Arrays;
import java.util.Date;

/*Напишите метод, который проверяет, входит ли в массив заданный элемент или нет.
Используйте перебор и двоичный поиск для решения этой задачи. Сравните время
выполнения обоих решений для больших массивов (например, 100000000 элементов).
*/
public class task2 {
    public static void main(String[] args) {
        int[] array = generateArray(10000000);
        Arrays.sort(array);
//        long nano_time = System.nanoTime();
//        System.out.println(System.nanoTime()-nano_time);
        long time = System.currentTimeMillis();
        search(array, 1);
        System.out.println("Поиск: "+(System.currentTimeMillis() - time));

        time = System.currentTimeMillis();
        binarySearchRecursion(array, 1, 0, array.length);
        System.out.println("Бинарный поиск: "+(System.currentTimeMillis() - time));
    }

    public static int search(int[] array, int key) {
        for (int i = 0; i < array.length; i++) {
            if (array[i] == key)
                return i;

        }

        return -1;
    }

    private static int binarySearchRecursion(int [] sortedArray, int key, int min, int max) {
        if (max < min) {
            return -1;
        }
        int middle = (min + max) / 2;

        if (key == sortedArray[middle]) {
            return middle;
        } else if (key < sortedArray[middle]) {
            return binarySearchRecursion(sortedArray, key, min, middle - 1);
        } else {
            return binarySearchRecursion(sortedArray, key, middle + 1, max);
        }
    }

    private static int[] generateArray(int length) {
        int[] array = new int[length];
        for (int i = 0; i < array.length; i++) {
            array[i] = (int) (Math.random()*10);
        }
        return array;
    }


}