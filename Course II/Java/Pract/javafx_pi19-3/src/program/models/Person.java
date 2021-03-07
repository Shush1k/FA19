package program.models;

import javafx.beans.property.*;

import java.time.LocalDate;

public class Person {
    private StringProperty firstName;
    private StringProperty lastName;
    private StringProperty street;
    private StringProperty city;
    private IntegerProperty postalCode;
    private ObjectProperty<LocalDate> birthDay;
    public Person(){
        this(null, null);
    }

    public Person(String firstName, String lastName){
        this.firstName = new SimpleStringProperty(firstName);
        this.lastName = new SimpleStringProperty(lastName);

        //Дефолт
        this.street = new SimpleStringProperty("Какая-то улица");
        this.city = new SimpleStringProperty("Какой-то город");
        this.postalCode = new SimpleIntegerProperty(1234);
        this.birthDay = new SimpleObjectProperty<LocalDate>(LocalDate.of(1995,9,12));
    }

    public String getFirstName() {
        return firstName.get();
    }

    public void setFirstName(String firstName) {
        this.firstName.set(firstName);
    }

    public void setLastName(String lastName) {
        this.lastName.set(lastName);
    }

    public void setStreet(String street) {
        this.street.set(street);
    }

    public void setCity(String city) {
        this.city.set(city);
    }

    public void setBirthDay(LocalDate birthDay) {
        this.birthDay.set(birthDay);
    }

    public void setPostalCode(int postalCode) {
        this.postalCode.set(postalCode);
    }

    public String getLastName() {
        return lastName.get();
    }

    public String getStreet() {
        return street.get();
    }

    public String getCity() {
        return city.get();
    }

    public int getPostalCode() {
        return postalCode.get();
    }

    public LocalDate getBirthDay() {
        return birthDay.get();
    }

    public StringProperty getFirstNameProperty() {
        return firstName;
    }

    public StringProperty getLastNameProperty() {
        return lastName;
    }

    public StringProperty getStreetProperty() {
        return street;
    }

    public StringProperty getCityProperty() {
        return city;
    }

    public IntegerProperty getPostalCodeProperty() {
        return postalCode;
    }

    public ObjectProperty<LocalDate> getBirthDayProperty() {
        return birthDay;
    }
}
