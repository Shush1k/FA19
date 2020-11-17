package com.work_5.task2;


class MyThread extends Thread {

    private Object lock;

    public MyThread(Object object) {
        this.lock = object;
    }

    @Override
    public void run() {
        for (int i=0;i<5;i++){
            synchronized (lock) {
                try {
                    System.out.println(getName());
                    lock.notify();
                    lock.wait();
                } catch (InterruptedException e) { }
                lock.notify();
            }
    }
    }
}

public class Main {
    public static void main(String[] strings) {
        Object lock = new Object();
        new MyThread(lock).start();
        new MyThread(lock).start();
    }
}