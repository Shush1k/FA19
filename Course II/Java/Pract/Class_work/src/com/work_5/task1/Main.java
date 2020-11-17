package com.work_5.task1;
/*Выведите состояние потока

1) Перед его запуском

2) После запуска

3) Во время выполнения

С использованием synchronized, notifyAll, wait. Для синхронизации использовать простой объект класса Object

4) WAITING

5) BLOCKED

6)) TIMED_WAITING

getState()


Задача 2

Реализуйте 2 потока, которые выводят на консоль свое имя по очереди*/
public class Main {
    public static void main(String[] args) throws InterruptedException {
        Object lock = new Object();
        Thread thread = new Thread() {
            @Override
            public void run() {
                try {
                    synchronized (lock) {
                        lock.notifyAll();
                        lock.wait();
                    }
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        };
        synchronized (lock){
            System.out.println(thread.getState());
            thread.start();
            System.out.println(thread.getState());
            lock.wait();
            System.out.println(thread.getState());
            lock.notifyAll();
            System.out.println(thread.getState());
        }
        try {
            thread.join();
        }catch (InterruptedException e){}
        System.out.println(thread.getState());
    }



}
