package com.work3_1;

public class Print implements Printable{
    private String author;
    private String name;

    public String getAuthor() {
        return author;
    }

    public String getName() {
        return name;
    }

    @Override
    public void print() {
        System.out.printf("%s (%s)", name, author);
    }
    public Print(String name, String author){
        this.author = author;
        this.name = name;
    }


}
