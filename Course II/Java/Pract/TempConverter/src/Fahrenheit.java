public class Fahrenheit implements Convert {

    @Override
    public double getConvertedValue(double value) {
        return value * 1.8 + 32;
    }
}
