package program.controllers;

import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.Label;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import program.Main;
import program.models.Person;
import program.utils.DateUtil;

public class PersonOverviewController {
    @FXML
    private TableView<Person> personTable;
    @FXML
    private TableColumn<Person, String> firstNameColumn;
    @FXML
    private TableColumn<Person, String> lastNameColumn;
    @FXML
    private Label firstNameLabel;
    @FXML
    private Label lastNameLabel;
    @FXML
    private Label streetLabel;
    @FXML
    private Label cityLabel;
    @FXML
    private Label postalCodeLabel;
    @FXML
    private Label birthdayLabel;

    private Main main;

    public PersonOverviewController(){}

    @FXML
    private void initialize(){
        firstNameColumn.setCellValueFactory(cellData -> cellData.getValue().getFirstNameProperty());
        lastNameColumn.setCellValueFactory(cellData -> cellData.getValue().getLastNameProperty());

        showPersonsOverviewDetails(null);
        personTable.getSelectionModel().selectedItemProperty().addListener(
                (observable, oldValue, newValue) -> showPersonsOverviewDetails(newValue));
    }

    public void setMain(Main main) {
        this.main = main;
        personTable.setItems(main.getPersonData());
    }
    @FXML
    private void handleDeletePerson() {
        int selectedIndex = personTable.getSelectionModel().getSelectedIndex();
        if (selectedIndex >= 0) {
            personTable.getItems().remove(selectedIndex);
        } else {
            Alert alert = new Alert(Alert.AlertType.WARNING);
            alert.initOwner(main.getPrimaryStage());
            alert.setTitle("Delete warning");
            alert.setHeaderText("Row person not selected");
            alert.setContentText("Please select a person to edit in the table.");
            alert.showAndWait();
        }
    }
    private void showPersonsOverviewDetails(Person person) {
        if (person != null) {
            firstNameLabel.setText(person.getFirstName());
            lastNameLabel.setText(person.getLastName());
            streetLabel.setText(person.getStreet());
            cityLabel.setText(person.getCity());
            postalCodeLabel.setText(Integer.toString(person.getPostalCode()));
            birthdayLabel.setText(DateUtil.format(person.getBirthDay())); //заглушка
        } else {
            firstNameLabel.setText("");
            lastNameLabel.setText("");
            streetLabel.setText("");
            cityLabel.setText("");
            postalCodeLabel.setText("");
            birthdayLabel.setText("");
        }
    }

    @FXML
    private void handleNewPerson() {
        Person newPerson = new Person();
        boolean okClicked = main.showPersonEditDialog(newPerson,"Add person");
        if (okClicked) {
            if (main.getPersonData().contains(newPerson)){
                System.out.println("Person");
            }
            main.getPersonData().add(newPerson);
        }


    }

    @FXML
    private void handleEditPerson() {
        Person selectedPerson = personTable.getSelectionModel().getSelectedItem();
        if (selectedPerson != null) {
            boolean okClicked = main.showPersonEditDialog(selectedPerson,"Edit person");
            if (okClicked) {
                showPersonsOverviewDetails(selectedPerson);
            }

        } else {
            // Ничего не выбрано
            Alert alert = new Alert(Alert.AlertType.WARNING);
            alert.initOwner(main.getPrimaryStage());
            alert.setTitle("Edit warning");
            alert.setHeaderText("Row person not selected");
            alert.setContentText("Please select a person to edit in the table.");
            alert.showAndWait();
        }
    }


}
