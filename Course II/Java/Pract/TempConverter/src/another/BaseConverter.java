package another;

import java.util.Arrays;

public class BaseConverter {

    private static final Character[] AvBase = {'K', 'C', 'F'};
    public double baseValue;
    private char base;

    BaseConverter(double baseValue) {
        base = 'C';
        this.baseValue = baseValue;
    }

    BaseConverter(double baseValue, boolean isFahr) {
        if (isFahr) {
            base = 'F';
        } else {
            base = 'K';
        }
        this.baseValue = baseValue;

    }

    public char getBase() {
        return base;
    }

    public int setBase(char base) {
        if (base == this.base)
            return (int) this.baseValue;
        if (Arrays.asList(AvBase).contains(base)) {
            switch (this.base) {
                case 'C':
                    if (base == 'F') {
                        this.baseValue = new CelToFahr().getConvertedValue(this.baseValue);
                    } else {
                        this.baseValue = new CelToKel().getConvertedValue(this.baseValue);
                    }
                    break;
                case 'F':
                    this.baseValue = new FahrToCel().getConvertedValue(this.baseValue);
                    break;
                case 'K':
                    this.baseValue = new KelToCel().getConvertedValue(this.baseValue);
                    break;
            }
            this.base = base;
            return (int) this.baseValue;
        } else {
            System.out.println("Uncorrectable base!");
            throw new ArithmeticException();
        }
    }
}
