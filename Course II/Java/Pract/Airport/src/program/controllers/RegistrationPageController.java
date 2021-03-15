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
    @FXML
    private TextField phoneField;

    private boolean okClicked = false;
    private Stage RegistrationStage;
    private Person person;
    private Main main;

    @FXML
    public void initialize(){
        /*Пока задокументируем*/
//        loginField.setText(null);
//        firstNameField.setText(null);
//        lastNameField.setText(null);
//        birthdayField.setValue(null);
//        sexField.setText(null);
//        seriesField.setText(null);
//        numberField.setText(null);
//        emailField.setText(null);
//        phoneField.setText(null);
//        passwordField.setText(null);
//        passwordRepeatField.setText(null);
        person = new Person();

    }
    public boolean isOkClicked(){return okClicked;}

    public void setRegistrationStage(Stage RegistrationStage){this.RegistrationStage = RegistrationStage;}

    @FXML
    private void handleCancel(){RegistrationStage.close();}

    @FXML
    private void handleRegistration(){
//        TODO действия после нажатия на кнопку Зарегистрироваться
        RegistrationStage.close();
    }

    public void setMain(Main main) {
        this.main = main;
    }
}

