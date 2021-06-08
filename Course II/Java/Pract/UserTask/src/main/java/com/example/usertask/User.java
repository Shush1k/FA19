package com.example.usertask;

import lombok.AllArgsConstructor;
import lombok.Data;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


@Data
@AllArgsConstructor
public class User {

    private int id;
    private String name;
    private int age;
    private Sex sex;
    private static Map<Integer, User> AllUsers = new HashMap<>();

    public static Map<Integer, User> getAllUsers() {
        return AllUsers;
    }

    /**
     * Возвращаем список пользовтаелей по полу
     *
     * @param inputSex
     * @return
     */
    public List<User> getUsers(Sex inputSex) {
        List<User> resultList = new ArrayList<>();
        for (User user : AllUsers.values()) {
            if (user.getSex().equals(inputSex)) {
                resultList.add(user);
            }
        }
        return resultList;
    }

    /**
     * Возвращаем список всехх пользователей
     *
     * @return
     */
    public List<User> getUsers() {
        System.out.println(AllUsers.values());
        return new ArrayList<User>(AllUsers.values());
    }

    /**
     * Возвращаем кол-во пользователей
     *
     * @return
     */
    public int getUsersCount() {
        return AllUsers.size();
    }

    /**
     * Возвращаем кол-во пользователей по полу
     *
     * @return
     */
    public int getUsersCount(Sex inputSex) {
        return getUsers(inputSex).size();
    }

    /**
     * Подсчет среднего возраста из общего списка
     *
     * @return
     */
    public double getUsersMiddleAge() {
        long ageSum = 0;
        for (User user : AllUsers.values())
            ageSum += user.getAge();

        return (double) ageSum / AllUsers.size();
    }

    /**
     * Подсчет среднего возраста по полу
     *
     * @return
     */
    public double getUsersMiddleAge(Sex inputSex) {
        long ageSum = 0;
        int counter = 0;
        for (User user : AllUsers.values()) {
            if (user.getSex().equals(inputSex)) {
                ageSum += user.getAge();
                counter++;
            }
        }
        return (double) ageSum / counter;
    }

    /**
     * Сравнение двух пользователей
     *
     * @param firstUser
     * @param secondUser
     * @return
     */
    public boolean equals(User firstUser, User secondUser) {
        return firstUser.equals(secondUser);
    }

    public boolean equals(User otherUser) {
        return (otherUser.getName().equals(this.getName()) && (otherUser.getAge() == this.getAge()) && (otherUser.getSex() == this.getSex()));
    }


    @Override
    public String toString() {
        return "User{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", age=" + age +
                ", sex='" + sex + '\'' +
                '}';
    }
}