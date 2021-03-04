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
    private BorderPane mainLayout;
    private ObservableList<Person> personData = FXCollections.observableArrayList();

    public Main(){}

    public ObservableList<Person> getPersonData() {
        return personData;
    }

    @Override
    public void start(Stage primaryStage) throws Exception {
        this.primaryStage = primaryStage;
//        this.primaryStage.setTitle("Airport");
//        TODO придумать как связать RootLayout и переход в MainLayout

        initRootLayout();
        showAuthorizationPage();
    }
    @FXML
    public void initRootLayout() {
        try {
            /*Панель меню, вкладка помощь*/
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
    public void MainLayout() {
        try {
//            TODO сделать из этого MainLayout по аналогии с RootLayout Toolbar а внутри 3 окна (прилет, вылет, авиакомпании)
            FXMLLoader loader = new FXMLLoader();
            loader.setLocation(Main.class.getResource("views/mainLayout.fxml"));
            mainLayout = (BorderPane) loader.load();

            Scene scene = new Scene(mainLayout);
            Stage mainStage = new Stage();
            mainStage.setScene(scene);
            mainStage.setResizable(false);

            MainLayoutController mainLayoutController = loader.getController();
            mainLayoutController.setMain(this);
            mainStage.show();
        } catch (IOException e){
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

            /*В центре страница авторизации*/
            rootLayout.setCenter(authorizationPage);

            AuthorizationController controller = loader.getController();
            controller.setMain(this);
        }catch (IOException e){
            e.printStackTrace();
        }
    }
    public void showRegistrationPage() {
        try {
            /* Отображение отдельного окна Регистрация*/
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
            /* Отображение сцены Автор*/
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
            /* Отображение сцены Изменение данных*/
            FXMLLoader loader = new FXMLLoader();
            loader.setLocation(Main.class.getResource("views/editPerson.fxml"));
            AnchorPane editPersonPage = (AnchorPane) loader.load();
            Stage stage = new Stage();
            stage.setTitle("Изменение данных");
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

    public void showArrivalBoardPage(){
        try {
            /* Отображение сцены Табло прилета*/
            FXMLLoader loader = new FXMLLoader();
            loader.setLocation(Main.class.getResource("views/arrivalboard.fxml"));
            BorderPane arrivalBoardPage = (BorderPane) loader.load();

            /*В центре страницы Табло прилета*/
            mainLayout.setCenter(arrivalBoardPage);

            ArrivalBoardController controller = loader.getController();
            controller.setMain(this);
        } catch (IOException e){
            e.printStackTrace();
        }
    }

    public void showDepartureBoardPage(){
        try {
            /* Отображение сцены Табло вылета*/
            FXMLLoader loader = new FXMLLoader();
            loader.setLocation(Main.class.getResource("views/departureboard.fxml"));
            BorderPane departureBoardPage = (BorderPane) loader.load();

            /*В центре страницы Табло вылета*/
            mainLayout.setCenter(departureBoardPage);

            DepartureBoardController controller = loader.getController();
            controller.setMain(this);
        } catch (IOException e){
            e.printStackTrace();
        }
    }
    public void showAirlineInfoPage(){
        try {
            /* Отображение сцены Информация авиакомпаний*/
            FXMLLoader loader = new FXMLLoader();
            loader.setLocation(Main.class.getResource("views/airlineInfo.fxml"));
            BorderPane airlineInfoPage = (BorderPane) loader.load();

            /*В центре страницы Информация авиакомпаний*/
            mainLayout.setCenter(airlineInfoPage);

            AirlineInfoController controller = loader.getController();
            controller.setMain(this);
        } catch (IOException e){
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        launch(args);
    }
}
