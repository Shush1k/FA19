package com.work3_2_teacher;

public class CelToFahr implements Converter{
    @Override
    public double getConvertedValue(double baseValue) {
        return 1.8 * baseValue + 32;
    }
}
