package program.utils;

import javafx.scene.control.Alert;
import javafx.stage.Stage;

public abstract class Alerts {
    public static void showNoValidSignIn(Stage stage){
        Alert alert = new Alert(Alert.AlertType.ERROR);
        alert.initOwner(stage);
        alert.setTitle("Ошибка входа");
        alert.setHeaderText("Некорректный логин или пароль");
        alert.setContentText("Введите корректные данные или зарегистрируйтесь!");
        alert.showAndWait();
    }
    public static void showNoValidInput(Stage stage, String errorMessage) {
        /* Если пользователь вводит то, чего не должен*/
        Alert alert = new Alert(Alert.AlertType.ERROR);
        alert.initOwner(stage);
        alert.setTitle("Ошибка ввода");
        alert.setHeaderText("Измените некорректно заполненные поля");
        alert.setContentText(errorMessage);
        alert.showAndWait();
    }

    public static void shoNoValidEmail(Stage stage){
        /* Если пользователь вводит некорректный Email*/
        Alert alert = new Alert(Alert.AlertType.ERROR);
        alert.initOwner(stage);
        alert.setTitle("Формат почты");
        alert.setHeaderText("Введите корректную электронную почту!");
        alert.setContentText("Пример почты: jakobknight@mail.ru");
        alert.showAndWait();
    }

    public static void shoNoValidPhoneNumber(Stage stage){
        /* Если пользователь вводит некорректный номер телефона*/
        Alert alert = new Alert(Alert.AlertType.ERROR);
        alert.initOwner(stage);
        alert.setTitle("Формат номера телефона");
        alert.setHeaderText("Введите номер телефона в указанном формате");
        alert.setContentText("Формат ввода: +7{номер телефона} или 8{номер телефона}");
        alert.showAndWait();
    }

}
