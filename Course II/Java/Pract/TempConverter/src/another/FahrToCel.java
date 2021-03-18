package another;

public class FahrToCel implements Converter {
    @Override
    public double getConvertedValue(double baseValue) {
        return (baseValue - 32) / 1.8;
    }
}
