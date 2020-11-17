package com.work_5.ThreadTasks;

public class Main {
    public static void main(String[] args) {

        System.out.println("Main started");
        //        for (int i = 0; i < 10; i++) {
//            new Thread("Thread1").start();
//            System.out.println("Main finish");
//        }
//        NewThread2 nt = new NewThread2();
//        NewThread t = new NewThread("Thread1");
//        nt.start();
////        t.start();
//
//        try {
//            Thread.sleep(1100);
//            nt.interrupt();
//            Thread.sleep(200);
////            t.join();
//        }catch (InterruptedException e){
//            System.out.printf("%s has been interrupted", t.getName());
//        }
        CommonResources commonResources = new CommonResources();
        for (int i=1;i<5;i++){
            Thread t = new Thread(new CountThread(commonResources), "Thread"+i);
            t.start();
        }
        System.out.println("Main thread finished");
    }
}
