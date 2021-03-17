

public class Main {
    public static void main(String[] args) {
        double temp = 10;

        System.out.println("Температура в Celsius: "+ new Celsius().getConvertedValue(temp));
        System.out.println("Температура в Fahrenheit: "+ new Fahrenheit().getConvertedValue(temp));
        System.out.println("Температура в Kelvin: "+ new Kelvin().getConvertedValue(temp));
    }

}
