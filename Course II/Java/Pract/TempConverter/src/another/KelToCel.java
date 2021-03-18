package another;

public class KelToCel implements Converter {
    @Override
    public double getConvertedValue(double baseValue) {
        return baseValue - 273.15;
    }
}
