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
//            primaryStage.setResizable(false);
            RootLayoutController rootLayoutController = loader.getController();
            rootLayoutController.setMain(this);
            primaryStage.show();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void showAuthorizationPage(){
        try{
            FXMLLoader loader = new FXMLLoader();
            loader.setLocation(Main.class.getResource("views/authorization.fxml"));
            AnchorPane authorizationPage = (AnchorPane) loader.load();
            rootLayout.setCenter(authorizationPage);
            AuthorizationController controller = loader.getController();
            controller.setMain(this);
        }catch (IOException e){
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        launch(args);
    }
}
