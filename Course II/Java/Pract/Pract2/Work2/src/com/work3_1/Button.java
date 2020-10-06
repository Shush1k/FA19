package com.work3_1;

public class Button {
    EventHandler handler;
    Button(EventHandler action){
        this.handler = action;

    }
    public void click(){
        System.out.println("Click");

    }
}
