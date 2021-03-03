package program;

import javafx.application.Application;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.layout.AnchorPane;
import javafx.scene.layout.BorderPane;
import javafx.stage.Modality;
import javafx.stage.Stage;
import program.controllers.*;
import program.models.Person;

import java.io.IOException;

public class Main extends Application {
    private Stage primaryStage;
    private BorderPane rootLayout;
    private ObservableList<Person> personData = FXCollections.observableArrayList();

    public Main(){}

    public ObservableList<Person> getPersonData() {
        return personData;
    }

    @Override
    public void start(Stage primaryStage) throws Exception {
        this.primaryStage = primaryStage;
        this.primaryStage.setTitle("Airport");

        initRootLayout();
        showAuthorizationPage();
    }
    @FXML
    public void initRootLayout() {
        try {
            FXMLLoader loader = new FXMLLoader();
            loader.setLocation(Main.class.getResource("views/rootLayout.fxml"));
            rootLayout = (BorderPane) loader.load();

            Scene scene = new Scene(rootLayout);
            primaryStage.setScene(scene);
            primaryStage.setResizable(false);
            RootLayoutController rootLayoutController = loader.getController();
            rootLayoutController.setMain(this);
            primaryStage.show();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void showAuthorizationPage(){
        try{
            /* Отображение сцены Авторизации
            * при закрытии окна, возвращает на RootLayout*/
            FXMLLoader loader = new FXMLLoader();
            loader.setLocation(Main.class.getResource("views/authorization.fxml"));
            AnchorPane authorizationPage = (AnchorPane) loader.load();
            Stage stage = new Stage();
            stage.setTitle("Авторизация");
            stage.initModality(Modality.WINDOW_MODAL);
            stage.initOwner(primaryStage);
            stage.setResizable(false);

            Scene scene = new Scene(authorizationPage);
            stage.setScene(scene);

            AuthorizationController controller = loader.getController();
            controller.setAuthorizationStage(stage);
            controller.setMain(this);
            stage.showAndWait();
        }catch (IOException e){
            e.printStackTrace();
        }
    }
    public void showRegistrationPage() {
        try {
            /* Отображение сцены Регистрация
             * при закрытии окна, возвращает на Авторизацию*/
            FXMLLoader loader = new FXMLLoader();
            loader.setLocation(Main.class.getResource("views/registration.fxml"));
            AnchorPane registrationPage = (AnchorPane) loader.load();
            Stage stage = new Stage();
            stage.setTitle("Регистрация");
            stage.initModality(Modality.WINDOW_MODAL);
            stage.initOwner(primaryStage);
            stage.setResizable(false);

            Scene scene = new Scene(registrationPage);
            stage.setScene(scene);

            RegistrationPageController controller = loader.getController();
            controller.setRegistrationStage(stage);
            controller.setMain(this);
            stage.showAndWait();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void showAboutPage(){
        try {
            /* Отображение сцены Автор
             * при закрытии окна, возвращает на ...*/
            FXMLLoader loader = new FXMLLoader();
            loader.setLocation(Main.class.getResource("views/aboutPage.fxml"));
            AnchorPane aboutPage = (AnchorPane) loader.load();
            Stage stage = new Stage();
            stage.setTitle("Автор");
            stage.initModality(Modality.WINDOW_MODAL);
            stage.initOwner(primaryStage);
            stage.setResizable(false);

            Scene scene = new Scene(aboutPage);
            stage.setScene(scene);

            AboutPageController controller = loader.getController();
            controller.setAboutStage(stage);
            stage.showAndWait();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void showEditPersonPage(){
        try {
            /* Отображение сцены Изменения данных*/
            FXMLLoader loader = new FXMLLoader();
            loader.setLocation(Main.class.getResource("views/editPerson.fxml"));
            AnchorPane editPersonPage = (AnchorPane) loader.load();
            Stage stage = new Stage();
            stage.setTitle("Изменения данных");
            stage.initModality(Modality.WINDOW_MODAL);
            stage.initOwner(primaryStage);
            stage.setResizable(false);

            Scene scene = new Scene(editPersonPage);
            stage.setScene(scene);

            EditPersonController controller = loader.getController();
            controller.setEditPersonStage(stage);
            stage.showAndWait();
        } catch (IOException e){
            e.printStackTrace();
        }
    }


    public static void main(String[] args) {
        launch(args);
    }
}
