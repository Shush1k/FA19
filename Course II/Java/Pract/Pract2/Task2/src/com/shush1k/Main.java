package com.shush1k;

public class Main {

    public static void main(String[] args) {
        Vector vector1 = new Vector(3, 4, 5);
        Vector vector2 = new Vector(3, 6, 10);
        System.out.println("Вектор 1:");
	    vector1.getValue();
        System.out.println("Вектор 2:");
        vector2.getValue();
	    System.out.println("\nДлина вектора 1:\n"+vector1.Len());
	    System.out.println("Скалярное произведение:\n"+vector1.Scalar(vector2));
        System.out.println("Векторное произведение:\n");
        vector1.Multi(vector2).getValue();
        System.out.println("Косинус угла:\n"+vector1.VectorAngle(vector2));
        System.out.println("Сумма двух векторов:");
        vector1.Sum(vector2).getValue();
        System.out.println("Разность двух векторов:");
        vector1.Diff(vector2).getValue();
        System.out.println("Массив векторов:");
        Vector[] vectors = Vector.VectorGen(4);
        for (int i = 0; i < vectors.length; i++) {
            vectors[i].getValue();
        }
    }

}
