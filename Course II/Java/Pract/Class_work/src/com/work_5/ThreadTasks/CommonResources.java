package com.work_5.ThreadTasks;

public class CommonResources {
    int x;

    synchronized void increment() {
        x = 1;
        for (int i = 1; i < 5; i++) {
            System.out.printf("%s %d \n", Thread.currentThread().getName(), x);
            x++;
            try {
                Thread.sleep(200);
            } catch (InterruptedException e) {}
        }
    }
}