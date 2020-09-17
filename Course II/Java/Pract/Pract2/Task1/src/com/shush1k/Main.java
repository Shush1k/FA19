package com.shush1k;

public class Main {

    public static void main(String[] args) {
        Matrix obj1 = new Matrix(2, 4);
        Matrix obj2 = new Matrix(2, 4);
        System.out.println("Матрица 1:");
        obj1.getValue();
        System.out.println("\nМатрица 2:");
        obj2.getValue();


        MatrixExe objExe = new MatrixExe(obj1, obj2);
        System.out.println("\nСумма:");
        Matrix result = objExe.Sum();
        if (result != null) {
            result.getValue();
        }

        System.out.println("\nРазность:");
        result = objExe.Diff();
        if (result != null) {
            result.getValue();
        }
        Matrix obj3 = new Matrix(4, 2);
        Matrix obj4 = new Matrix(2, 4);

        System.out.println("\nМатрица 3:");
        obj3.getValue();
        System.out.println("\nМатрица 4:");
        obj4.getValue();

        System.out.println("\nПроизведение:");
        MatrixExe objExe2 = new MatrixExe(obj3, obj4);
        result = objExe2.Multiplier();
        if (result != null) {
            result.getValue();
        }
        //double не будет работать с матрицой, потому что тип данных матрицы int. Конфликт типов данных.
        int inpNumb = 2;
        System.out.println("\nУмножение матрицы 3 на число: " + inpNumb);
        result = obj3.numbMulti(inpNumb);
        if (result != null) {
            result.getValue();
        }

        System.out.println("\nТранспонированная матрица 1:");
        Matrix tran_obj1 = obj1.transposed();
        tran_obj1.getValue();

        System.out.println("\nМатрица 5(квадратная):");
        Matrix obj5 = new Matrix(2, 2);
        obj5.getValue();
        int exp = 2;
        System.out.println("\nВозведение матрицы 5 в степень " + exp + ":");
        result = obj5.exponentiation(exp);
        if (result != null) {
            result.getValue();
        }
    }
}
