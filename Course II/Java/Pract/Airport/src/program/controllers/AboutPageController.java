package program.controllers;

import javafx.application.HostServices;
import javafx.fxml.FXML;
import javafx.scene.control.Hyperlink;
import javafx.stage.Stage;

public class AboutPageController {
    @FXML
    private Hyperlink vkLink;
    @FXML
    private Hyperlink githubLink;

    private Stage stage;
    private HostServices hostServices;

    public HostServices getHostServices(){return hostServices;}

    public void setAboutStage(Stage stage) { this.stage = stage;}

    public void setHostServices(HostServices hostServices) {
        this.hostServices = hostServices;
    }

    @FXML
    public void initialize(){
        vkLink = new Hyperlink("https://vk.com/shush1k_s");
        githubLink = new Hyperlink("https://github.com/Shush1k");
    }

    @FXML
    public void openVk(){
        hostServices.showDocument(vkLink.getText());
    }
    @FXML
    public void openGithub(){
        hostServices.showDocument(githubLink.getText());
    }


    @FXML
    public void handleBackBtn(){
        stage.close();
    }
}
