package com.work_5.task1;

public class MyThread extends Thread{
    MyThread(String name){
        super(name);

    }
    public void run(){
        System.out.printf("%s started\n", Thread.currentThread().getName());
        try {
            Thread.sleep(100);
        }catch (InterruptedException e){
            System.out.println("Thread has been interrupted");
            interrupt();
        }
        System.out.printf("Thread %s is finished\n", Thread.currentThread().getName());
    }
}
