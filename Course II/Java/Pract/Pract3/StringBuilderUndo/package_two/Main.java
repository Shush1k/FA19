package package_two;

public class Main {
    public static void main(String[] strings) {
        ObservableStringBuilder observableStringBuilder =
                new ObservableStringBuilder();
        observableStringBuilder.setChangeListener(new Listener());
        observableStringBuilder.append("Привет");
        observableStringBuilder.append(", слушатель!");
        observableStringBuilder.replace(0, 6, "Пока");
    }
}
