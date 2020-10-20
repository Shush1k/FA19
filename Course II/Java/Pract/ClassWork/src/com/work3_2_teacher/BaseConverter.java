package com.work3_2_teacher;


import java.util.Arrays;

public class BaseConverter {

    public double baseValue;
    private char base;
    private static Character[] AvBase = {'K', 'C', 'F'};

    BaseConverter(double baseValue){
        base = 'C';
        this.baseValue = baseValue;
    }
    BaseConverter(double baseValue, boolean isFahr){
        if(isFahr){
            base = 'F';
            this.baseValue = baseValue;
        }
        else{
            base = 'K';
            this.baseValue = baseValue;
        }

    }

    public char getBase() {
        return base;
    }

    public int setBase(char base){
        if(base == this.base)
            return (int) this.baseValue;
        if(Arrays.asList(AvBase).contains(base)) {
            switch(this.base){
                case 'C':
                    if(base == 'F'){
                        this.baseValue = new CelToFahr().getConvertedValue(this.baseValue);
                    }
                    else{
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
        }
        else{
            System.out.println("Uncorrectable base!");
            throw new ArithmeticException();
        }
    }
}
