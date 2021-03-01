package program.models;

import javafx.beans.property.*;

import java.time.LocalDate;

public class Person {
    private final StringProperty login;
    private final StringProperty firstName;
    private final StringProperty lastName;
    private final StringProperty sex;
    private final StringProperty email;
    private final StringProperty phoneNumber;
    private final ObjectProperty<LocalDate> birthday;
    private final StringProperty seriesPassport;
    private final StringProperty numberPassport;
    private final StringProperty password;
    private final StringProperty repeatPassword;

    public Person() { this(null, null, null, null, null, null, null, null, null, null, null); }

    public Person(String login,
                  String firstName,
                  String lastName,
                  String sex,
                  LocalDate birthday,
                  String seriesPassport,
                  String numberPassport,
                  String phoneNumber,
                  String email,
                  String password,
                  String repeatPassword) {
        this.login = new SimpleStringProperty(login);
        this.firstName = new SimpleStringProperty(firstName);
        this.lastName = new SimpleStringProperty(lastName);
        this.sex = new SimpleStringProperty(sex);
        this.birthday = new SimpleObjectProperty(birthday);
        this.seriesPassport = new SimpleStringProperty(seriesPassport);
        this.numberPassport = new SimpleStringProperty(numberPassport);
        this.email = new SimpleStringProperty(email);
        this.phoneNumber = new SimpleStringProperty(phoneNumber);
        this.password = new SimpleStringProperty(password);
        this.repeatPassword = new SimpleStringProperty(repeatPassword);
    }
    public Person(String login,
                  String firstName,
                  String lastName,
                  String sex,
                  LocalDate birthday,
                  String seriesPassport,
                  String numberPassport,
                  String phoneNumber,
                  String password,
                  String repeatPassword) {
        this(login, firstName, lastName, sex, birthday, seriesPassport, numberPassport, phoneNumber,null, password, repeatPassword);
    }

    public String getFirstName() {
        return firstName.get();
    }

    public String getLastName() {
        return lastName.get();
    }

    public String getLogin() {
        return login.get();
    }

    public LocalDate getBirthday() {
        return birthday.get();
    }

    public String getSex() {
        return sex.get();
    }

    public String getEmail() {
        return email.get();
    }

    public String getSeriesPassport() {
        return seriesPassport.get();
    }

    public String getNumberPassport() {
        return numberPassport.get();
    }

    public String getPhoneNumber() {
        return phoneNumber.get();
    }

    public String getPassword() {
        return password.get();
    }

    public String getRepeatPassword() {
        return repeatPassword.get();
    }

    public void setLogin(String login){this.login.set(login);}

    public void setFirstName(String firstName){this.login.set(firstName);}

    public void setLastName(String lastName){this.login.set(lastName);}

    public void setBirthday(LocalDate birthday){this.login.set(String.valueOf(birthday));}

    public void setSex(String sex){this.login.set(sex);}

    public void setEmail(String email){this.login.set(email);}

    public void setSeriesPassport(String seriesPassport){this.login.set(seriesPassport);}

    public void setNumberPassport(String numberPassport){this.login.set(numberPassport);}

    public void setPhoneNumber(String phoneNumber){this.login.set(phoneNumber);}

    public void setPassword(String password){this.login.set(password);}

    public void setRepeatPassword(String repeatPassword){this.login.set(repeatPassword);}

    @Override
    public String toString() {
        return "Person{" +
                "login=" + login +
                ", firstName=" + firstName +
                ", lastName=" + lastName +
                ", sex=" + sex +
                ", email=" + email +
                ", phoneNumber=" + phoneNumber +
                ", birthday=" + birthday +
                ", seriesPassport=" + seriesPassport +
                ", numberPassport=" + numberPassport +
                ", password=" + password +
                ", repeatPassword=" + repeatPassword +
                '}';
    }
}
