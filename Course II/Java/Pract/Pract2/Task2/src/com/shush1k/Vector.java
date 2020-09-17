package com.shush1k;
import java.util.Random;
/*Создайте класс, который описывает вектор (в трёхмерном пространстве).
У него должны быть:
a. конструктор с параметрами в виде списка координат x, y, z
b. метод, вычисляющий длину вектора. Корень можно посчитать с помощью
Math.sqrt()
c. метод, вычисляющий скалярное произведение
d. метод, вычисляющий векторное произведение с другим вектором
e. метод, вычисляющий угол между векторами (или косинус угла): косинус угла
между векторами равен скалярному произведению векторов, деленному на
произведение модулей (длин) векторов
f. методы для суммы и разности
g. статический метод, который принимает целое число N, и возвращает массив
случайных векторов размером N
h. Если метод возвращает вектор, то он должен возвращать новый объект, а не
менять базовый*/
public class Vector {
    int x;
    int y;
    int z;
    public Vector(int x, int y, int z){
        this.x = x;
        this.y = y;
        this.z = z;
    }
    public void getValue(){
        // Вывод вектора
        System.out.format("(%d, %d, %d)\n", x, y, z);
    }
    public double Len(){
        // Длина вектора
        return Math.sqrt(Math.pow(x, 2)+ Math.pow(y, 2)+ Math.pow(z, 2));
    }
    public double Scalar(Vector vector){
        // Скалярное пр-ие
        return x*vector.x + y*vector.y + z*vector.z;
    }
    public Vector Multi(Vector vector){
        // Векторное пр-ие
        return new Vector(y*vector.z - z*vector.y,z*vector.x - x*vector.z, x*vector.y - y*vector.x);
    }
    public double VectorAngle(Vector vector){
        // Угол между векторами
        return Scalar(vector)/ (Math.abs(vector.Len())*Math.abs(Len()));

    }
    //Сумма и разность
    public Vector Sum(Vector vector){
        return new Vector(x+vector.x, y+vector.y, z+vector.z);
    }
    public Vector Diff(Vector vector){
        return new Vector(x-vector.x, y-vector.y, z-vector.z);
    }
    public static Vector[] VectorGen(int N){
        // Массив векторов
        Vector[] arr;
        arr = new Vector[N];
        for (int i=0; i<N;i++){
            Random numb = new Random();
            int X = numb.nextInt(100);
            int Y = numb.nextInt(100);
            int Z = numb.nextInt(100);
            arr[i] = new Vector(X,Y,Z);
        }
        return arr;

    }
}
