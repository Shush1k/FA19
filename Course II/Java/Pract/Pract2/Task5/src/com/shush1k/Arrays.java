package com.shush1k;
/*Напишите класс, конструктор которого принимает два массива: массив значений и массив весов значений.
Класс должен содержать метод, который будет возвращать элемент из первого массива случайным образом, с учётом его веса.
Пример:
Дан массив [1, 2, 3], и массив весов [1, 2, 10].
В среднем, значение «1» должно возвращаться в 2 раза реже, чем значение «2» и в десять раз реже, чем значение «3».
 */
public class Arrays {
    int[] new_arr;
    /*создаем третий массив, пример:
        Вход: ([1,2,3], [1,2, 10])
        Сделать: [1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        Вернуть: рандомный элемент из массива!*/
    public Arrays(int[] values, int[] scales){
        int sum = 0;
        // Длина нового массива
        for (int i : scales) {
            sum += i;
        }
        new_arr = new int[sum];
        // Добавляем элементы в массив
        int k = 0;
        System.out.print("Массив: ");
        for(int i = 0; i < scales.length; i++){
            for(int j = 0; j < scales[i]; j++) {
                new_arr[k] = values[i];
                k += 1;
            }
        }
        System.out.println(java.util.Arrays.toString(new_arr));

        }
    public void getRandom(){
        double random =  (int)(Math.random() * new_arr.length-1);
        System.out.println("\nПолученный элемент: "+new_arr[(int) random]);
    }

}

