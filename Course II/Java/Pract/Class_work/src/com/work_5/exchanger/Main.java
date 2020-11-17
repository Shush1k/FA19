package com.work_5.exchanger;

import java.util.concurrent.Exchanger;
/*Exchanger обмен данными между потоками*/
public class Main {
    public static void main(String[] args) {
        Exchanger<String> exchanger = new Exchanger<>();
        new Thread(new PutThread(exchanger)).start();
        new Thread(new GetThread(exchanger)).start();
    }
}
