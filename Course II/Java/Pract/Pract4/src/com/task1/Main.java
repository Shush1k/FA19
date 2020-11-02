/*
Создать 3 класса(базовый и 2 предка) которые описывают некоторых работников с
почасовой оплатой (один из предков) и фиксированой оплатой (второй предок).
a. Описать в базовом классе абстрактный метод для расчета среднемесячной
зарплаты.
b. Для «почасовщиков» формула для расчета такая: «среднемесячная зарплата =
20.8*8*ставка в час»,
c. для работников с фиксированой оплатой «среднемесячная зарплата =
фиксированой месячной оплате».
i. a)Упорядочить всю последовательность рабочих по убыванию
среднемесячной зарплаты.
ii. При совпадении зарплаты – упорядочить данные в алфавитном порядке по
имени. Вывести идентификатор работника,
iii. имя и среднемесячную зарплату для всех елементов списка.
iv. b)Вывести первые 5 имен работников из полученого выше списка
(задача А).
v. c)Вывести последние 3 идентификаторы работников из полученого више
списка (задача А).
vi. d)Организовать запись и чтение колекции в/из файл(а)
vii. e)Организовать обработку некоректного формата входного файла
*/

package com.task1;
import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashSet;


public class Main {

    public static void main(String[] args) throws IOException {
        boolean readable = true;

        ArrayList<worker> workerList = new ArrayList<>();

        if(readable){
            workerList = Main.readFile("Pract4//src//com//task1//data.txt");
        }
        else{
            //Добавляем сотрудников в список
            workerList.add(new hourWorker(73, "Baranov", 300));
            workerList.add(new fixedWorker(24, "Ivanov", 45000));
            workerList.add(new fixedWorker(31, "Kuznecov", 45000));
            workerList.add(new fixedWorker(48, "Rumyancev", 60000));
            workerList.add(new fixedWorker(15, "Simonov", 95000));
        }

        if(workerList.size() != 0){
            // Сортировка списка
            workerList.sort(Comparator.comparing(worker::calculateSalary, Collections.reverseOrder()).thenComparing(worker::getName));
            System.out.println("\nTop 5:");
            for (int i = 0; i < 5; i++) {
                System.out.println(workerList.get(i).getName());
            }
            System.out.println("\nLast 3:");
            for (int i = workerList.size() - 1; i > workerList.size() - 4; i--) {
                System.out.println(workerList.get(i).getId());
            }
            System.out.println();

            Main.printList(workerList);
            Main.writeToFile(workerList);
        }
        else{
            System.out.println("Can`t read file!");
        }


    }

    public static void printList(ArrayList<worker> workerList) {
        for (worker w: workerList) {
            System.out.println(w.getId() + " " + w.getName() + " " + (int)w.getSalary()+" "+ w.calculateSalary());
        }
    }

    public static void writeToFile(ArrayList<worker> workerList) throws IOException {
        FileWriter writer = new FileWriter("Pract4//src//com//task1//data.txt");
        for (worker w : workerList) {
            writer.write(w.getId() + " " + w.getName() + " " + (int)w.getSalary() + "\n");
        }
        writer.flush();
    }

    public static ArrayList<worker> readFile(String path) throws IOException{
        ArrayList<worker> workerList = new ArrayList<>();
        HashSet<Integer> id_workerList = new HashSet<>();
        try {
            FileReader fr = new FileReader(path);
            BufferedReader reader = new BufferedReader(fr);
            String line = reader.readLine();
            while (line != null) {
                int id = Integer.parseInt(line.split(" ")[0]);
                if(id_workerList.contains(id)){
                    id+=1;
                }

                String name = line.split(" ")[1];

                if(name.length() == 0){
                    throw new Exception();
                }
                int status = Integer.parseInt(line.split(" ")[2]);
                System.out.println(status);
                if(status<5000){
                    System.out.println("hour worker added!");
                    workerList.add(new hourWorker(id,name,status));
                }
                else{
                    System.out.println("fixed worker added!");
                    workerList.add(new fixedWorker(id,name,status));
                }
                line = reader.readLine();
            }
            return workerList;

        }
        catch (IOException ex){
            System.out.print("\nReadable exception");
            return workerList;
        }
        catch (Exception ex){
            System.out.print("\nExcept exception");
            return workerList;
        }
    }


}


