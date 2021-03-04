package program.controllers;

import javafx.fxml.FXML;
import javafx.stage.Stage;
import program.Main;

public class MainLayoutController {
    /*Данный класс контроллер нужен для управлением ToolBar*/
    private Main main;
//    TODO переход из одной страницы на другую по кнопкам ToolBar

    @FXML
    public void openArrivalBoard() {
        main.showArrivalBoardPage();
    }
    @FXML
    public void openDepartureBoard() {
        main.showDepartureBoardPage();
    }
    @FXML
    public void openAirlineInfo() {
        main.showAirlineInfoPage();
    }

    public void setMain(Main main) {
        this.main = main;
    }
}
