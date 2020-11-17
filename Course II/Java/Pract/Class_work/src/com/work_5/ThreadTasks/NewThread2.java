package com.work_5.ThreadTasks;

public class NewThread2 implements Runnable{
    private boolean isActive;

    public void disable(){
        isActive = false;
    }
    NewThread2(){
        isActive = true;
    }
    @Override
    public void run(){
        System.out.printf("%s started\n", Thread.currentThread().getName());
        int counter = 1;
        while (isActive){
            System.out.println("Loop"+counter++);
            try {
                Thread.sleep(200);
            }
            catch (InterruptedException e){
                System.out.println("Thread is interrupted");
            }
        }

        System.out.printf("Thread %s is finished\n", Thread.currentThread().getName());
    }
}
