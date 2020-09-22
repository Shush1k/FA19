package com.shush1k;

public class MatrixExe {
    Matrix obj1;
    Matrix obj2;
    public MatrixExe(Matrix obj1, Matrix obj2){
        this.obj1 = obj1;
        this.obj2 = obj2;
    }
    public Matrix Sum() {
        if ((obj1.n != obj2.n) || (obj1.m != obj2.m)) {
            System.out.println("Неправильная размерность матриц");
            return null;
        } else {
            int[][] res = new int[obj1.n][obj2.m];
            for (int i = 0; i < obj1.n; i++){
                for (int j = 0; j < obj2.m; j++){
                    res[i][j] = obj1.matrix[i][j] + obj2.matrix[i][j];
                }
            }

            return new Matrix(res);
        }

    }
    public Matrix Diff(){
        if ((obj1.n != obj2.n) || (obj1.m != obj2.m)) {
            System.out.println("Неправильная размерность матриц");
            return null;
        } else {
            int[][] res = new int[obj1.n][obj2.m];
            for (int i = 0; i < obj1.n; i++){
                for (int j = 0; j < obj2.m; j++){
                    res[i][j] = obj1.matrix[i][j] - obj2.matrix[i][j];
                }
            }

            return new Matrix(res);
        }
    }
    // умножение
    public Matrix Multiplier() {
        if (obj1.m != obj2.n) {
            System.out.println("Неправильная размерность матриц");
            return null;
        }
        else {
            int[][] res = new int[obj1.n][obj2.m];
            for (int i = 0; i < obj1.n; i++){
                for (int j = 0; j < obj2.m; j++){
                    for (int v = 0; v < obj1.m; v++){
                        res[i][j] += obj1.matrix[i][v] * obj2.matrix[v][j];
                    }
            }
            }
            return new Matrix(res);
        }
    }
}
