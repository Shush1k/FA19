package com.shush1k;
import java.util.Random;
/*
1)	Реализуйте класс матрицы и методы
a.	Сложение и вычитание матриц.
b.	Умножение матрицы на число.
c.	Произведение двух матриц.
d.	Транспонированная матрица.
e.	Возведение матрицы в степень.
f.	Если метод, возвращает матрицу, то он должен возвращать новый объект, а не менять базовый.
 */
public class Matrix {
    int n;
    int m;
    int[][] matrix;
    // Первый конструктор класса
    public Matrix(int n, int m){
        this.n = n;
        this.m = m;
        this.matrix = new int[n][m];
        this.createMatrix();
    }
    // Второй конструктор класса
    public Matrix(int[][] matrix){
        this.matrix = matrix;
        this.n = matrix.length;
        this.m = matrix[0].length;

    }
    // Метод класса создание матрицы
    public void createMatrix(){
        Random random = new Random();
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                matrix[i][j] = random.nextInt(100);
            }
        }

    }
    // Вывод в консоль матрицы
    public void getValue() {
        for (int[] ints : matrix) {
            for (int anInt : ints) {
                System.out.print(anInt + "\t");
            }
            System.out.print("\n");
        }
    }
    // Умножение на число
    public Matrix numbMulti(int Number){
        int[][] res = new int[this.n][this.m];
        for (int i = 0; i < this.n; i++) {
            for (int j = 0; j < this.m; j++) {
                int result = this.matrix[i][j] * Number;
                res[i][j] = result;
            }
        }
        return new Matrix(res);
    }
    // Транспонированная
    public Matrix transposed(){
        int[][] res = new int[this.m][this.n];
        for (int i = 0; i < this.n; i++) {
            for (int j = 0; j < this.m; j++) {
                res[j][i] = matrix[i][j];
            }
        }
        return new Matrix(res);
    }
    public Matrix exponentiation(int exp){
        if (this.n != this.m){
            System.out.println("Матрица не квадратная!");
            return  null;
        }
        else {
            int exp_temp = 1;
            Matrix new_Matrix = this;
            Matrix curr_Matrix = this;
            while (exp_temp++ < exp){
                MatrixExe obj = new MatrixExe(new_Matrix, curr_Matrix);
                new_Matrix = obj.Multiplier();
            }
            return new_Matrix;
        }
    }
}
