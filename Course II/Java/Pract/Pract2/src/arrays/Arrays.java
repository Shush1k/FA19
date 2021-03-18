package arrays;


public class Arrays {
    int[] new_arr;

    /*создаем третий массив, пример:
        Вход: ([1,2,3], [1,2, 10])
        Сделать: [1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        Вернуть: рандомный элемент из массива!*/
    public Arrays(int[] values, int[] scales) {
        int sum = 0;
        // Длина нового массива
        for (int i : scales) {
            sum += i;
        }
        new_arr = new int[sum];
        // Добавляем элементы в массив
        int k = 0;
        System.out.print("Массив: ");
        for (int i = 0; i < scales.length; i++) {
            for (int j = 0; j < scales[i]; j++) {
                new_arr[k] = values[i];
                k += 1;
            }
        }
        System.out.println(java.util.Arrays.toString(new_arr));

    }

    public void getRandom() {
        double random = (int) (Math.random() * new_arr.length - 1);
        System.out.println("\nПолученный элемент: " + new_arr[(int) random]);
    }

}

