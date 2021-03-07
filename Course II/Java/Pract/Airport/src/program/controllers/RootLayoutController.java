package program.controllers;

import javafx.fxml.FXML;
import program.Main;

public class RootLayoutController {
    /*Данный класс контроллер нужен для управлением меню*/
    private Main main;
    @FXML
    private void handleAbout(){
        main.showAboutPage();
    }

    public void setMain(Main main) {
        this.main = main;
    }
}
