package com.work_5.exchanger;

import java.util.concurrent.Exchanger;

class GetThread implements Runnable{
    Exchanger<String> exchanger;
    String message;
    GetThread(Exchanger<String> exchanger){
        this.exchanger=exchanger;
        message = "Python!";
    }
    public void run(){
        try{
            message=exchanger.exchange(message);
            System.out.println("GetThread стал: " + message);
        }
        catch(InterruptedException ex){
            System.out.println(ex.getMessage());
        }
    }
}
