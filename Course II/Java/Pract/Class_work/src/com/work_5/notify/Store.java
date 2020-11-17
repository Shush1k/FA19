package com.work_5.notify;

public class Store {
    private int product =0;
    public synchronized void get(){
        while (product < 1){
            try {
                wait();
            }catch (InterruptedException e){}
        }
        product--;
        System.out.println("Клиент купил товар");
        System.out.printf("Товара на складе %d \n", product);
        notify();
    }
    public synchronized void put(){
        while (product>=3){
            try {
                wait();
            }catch (InterruptedException e){}
        }
        product++;
        System.out.println("Производитель добавил товар");
        System.out.printf("Товара на складе %d \n", product);
        notify();
    }
}
