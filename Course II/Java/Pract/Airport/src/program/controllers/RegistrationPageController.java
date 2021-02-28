package program.controllers;

import javafx.fxml.FXML;
import javafx.scene.control.DatePicker;
import javafx.scene.control.TextField;
import javafx.stage.Stage;
import program.Main;
import program.models.Person;


public class RegistrationPageController {
    @FXML
    private TextField firstNameField;
    @FXML
    private TextField lastNameField;
    @FXML
    private TextField loginField;
    @FXML
    private TextField passwordField;
    @FXML
    private TextField passwordRepeatField;
    @FXML
    private TextField sexField;
    @FXML
    private DatePicker birthdayField;
    @FXML
    private TextField seriesField;
    @FXML
    private TextField numberField;
    @FXML
    private TextField emailField;

    private boolean okClicked = false;
    private Stage stage;
    private Person person;
    private Main main;

    @FXML
    public void initialize(){
        firstNameField.setText(null);
        lastNameField.setText(null);
        loginField.setText(null);
        passwordField.setText(null);
        passwordRepeatField.setText(null);
        sexField.setText(null);
        birthdayField.setValue(null);
        seriesField.setText(null);
        numberField.setText(null);
        emailField.setText(null);
        person = new Person();

    }

}
