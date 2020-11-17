package com.work_5.exchanger;

import java.util.concurrent.Exchanger;

class PutThread implements Runnable{
    Exchanger<String> exchanger;
    String message;
    PutThread(Exchanger<String> exchanger){
        this.exchanger=exchanger;
        message = "Java!";
    }
    public void run(){
        try{
            message=exchanger.exchange(message);
            System.out.println("PutThread стал: " + message);
        }
        catch(InterruptedException ex){
            System.out.println(ex.getMessage());
        }
    }
}
