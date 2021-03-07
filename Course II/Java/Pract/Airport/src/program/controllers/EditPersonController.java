package program.controllers;

import javafx.fxml.FXML;

import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.stage.Stage;
import program.Main;
import program.models.Person;

public class EditPersonController {
    @FXML
    private Label loginLabel;
    //    TODO решить проблему с датой
    @FXML
    private Label birthdayLabel;
    @FXML
    private Label sexLabel;
    @FXML
    private TextField firstNameField;
    @FXML
    private TextField lastNameField;

    @FXML
    private TextField seriesField;
    @FXML
    private TextField numberField;
    @FXML
    private TextField phoneField;
    @FXML
    private TextField emailField;
    @FXML
    private TextField passwordField;
    @FXML
    private TextField repeatPasswordField;

    private boolean delete = false;
    private Stage editPersonStage;
    private Person person;
    private Main main;

    public void setPerson(Person person) {
        this.person = person;
        loginLabel.setText(this.person.getLogin());
        firstNameField.setText(this.person.getFirstName());
        lastNameField.setText(this.person.getLastName());
        birthdayLabel.setText(String.valueOf(this.person.getBirthday()));
        sexLabel.setText(this.person.getSex());
        seriesField.setText(this.person.getSeriesPassport());
        numberField.setText(this.person.getNumberPassport());
        emailField.setText(this.person.getEmail());
        phoneField.setText(this.person.getPhoneNumber());
        passwordField.setText(this.person.getPassword());
        repeatPasswordField.setText(this.person.getRepeatPassword());
    }

    public void setEditPersonStage(Stage editPersonStage) {
        this.editPersonStage = editPersonStage;
    }

    public Person getPerson() {
        return person;
    }

    public boolean isDelete(){return delete;}
    //  TODO действие обновление информации о персоне
    @FXML
    private void handleUpdate(){}
    @FXML
    private void handleCancel(){editPersonStage.close();}

    //  TODO действие удаления аккаунта
    @FXML
    private void handleDeleteAcc(){}

    private boolean isValidData(){
        // TODO проверка данных
        return false;
    }

    public void setMain(Main main){this.main = main;}
}
