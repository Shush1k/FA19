package com.work3_2_teacher;

public class FahrToCel implements Converter{
    @Override
    public double getConvertedValue(double baseValue) {
        return (baseValue-32) /1.8;
    }
}
