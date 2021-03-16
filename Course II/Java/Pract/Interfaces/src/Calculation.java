public interface Calculation {
    default int sum(int a, int b){
        return sumAll(a, b);
    }
    default int sum(int a, int b, int c){
        return sumAll(a, b, c);
    }
    private static int sumAll(int... values){
        int res = 0;
        for (int n:values){
            res+=n;
        }
        return res;
    }
}
