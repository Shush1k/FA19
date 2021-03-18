package another;

public class Main {
    public static void main(String[] args) {
        BaseConverter baseConverter = new BaseConverter(10);

        System.out.println(baseConverter.setBase('K'));
        System.out.println(baseConverter.setBase('F'));
        System.out.println(baseConverter.setBase('F'));
        System.out.println(baseConverter.setBase('C'));
    }
}
