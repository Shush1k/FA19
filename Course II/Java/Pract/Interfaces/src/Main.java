public class Main {
    public static void main(String[] args) {
        Print book = new Print("Ivan", "Ivanov");
        book.print();
        System.out.println("\n");
        Printable.read();

        Button button = new Button(new ButtonClickHandler());
        button.click();

        Calculation calculation = new Calculation() {
        };
        System.out.println(calculation.sum(2, 10));
    }
}



