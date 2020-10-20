package com.FilerTask;

import java.util.Arrays;
import java.util.function.Function;

public class Main {

    public static <T> T[] filter(T[] array, Function<? super T, Boolean> filter) {
        int offset = 0;

        for (int i = 0; i < array.length; i++) {
            if (!filter.apply(array[i])) {
                offset++;
            } else {
                array[i - offset] = array[i];
            }
        }
        return Arrays.copyOf(array, array.length - offset);
    }


    public static void main(String[] args) {
        String array[] =
                new String[]{"abc", "one", "double", null, "1"};

//        Не работает с int
//        int array[] = new int[]{1, 5, 2};
//        int[] newArray = filter(array, s -> s != 2);
        String newArray[] = filter(array, s -> s != null && s.length() <4);
        System.out.println(Arrays.toString(newArray));
    }
}

//public class Main {
//    public static void main(String[] args) {
//        Integer[] arr = new Integer[11];
//        fill(arr, integer -> (integer *5)); // 0, 1, 4, 9, 16 .....
//        System.out.println(Arrays.toString(arr));
//            }
//
//
//    public static <T> void fill(T[] objects, Function<Integer, ? extends T> function) {
//        for (int i = 0; i < objects.length; i++) {
//            objects[i] = function.apply(i);
//        }
//    }
//
//}