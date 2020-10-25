package package_two;

class Listener implements ChangeListener {

    @Override
    public void Change(ObservableStringBuilder stringBuilder) {
        System.out.println("Изменено: " + stringBuilder.toString());
    }
}
