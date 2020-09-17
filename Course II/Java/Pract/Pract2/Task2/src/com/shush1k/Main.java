package com.shush1k;

public class Main {

    public static void main(String[] args) {
        Vector vect1 = new Vector(3, 4, 5);
        Vector vect2 = new Vector(3, 6, 10);
        System.out.println("Вектор 1:");
	    vect1.getValue();
        System.out.println("Вектор 2:");
        vect2.getValue();
	    System.out.println("\nДлина вектора 1:\n"+vect1.Len());
	    System.out.println("Скалярное произведение:\n"+vect1.Scalar(vect2));
        System.out.println("Векторное произведение:\n");
        vect1.Multi(vect2).getValue();
        System.out.println("Косинус угла:\n"+vect1.VectorAngle(vect2));

    }

}
