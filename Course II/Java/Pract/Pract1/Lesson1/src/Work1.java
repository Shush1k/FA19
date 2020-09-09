public class Work1 {
    // Массивы
    public static void main(String[] args) {

        int[] nums = new int[5];
        int[] nums1 = new int[5];
        int[] nums2 = {1, 2, 3, 4, 5};
        //двумерный
        int[][] twoD = new int[5][4];
        int[][] twoD2 = new int[3][];
        for (int i = 0; i < 3; i++) {
            twoD2[i] = new int[i + 1];
        }
        int[][] twoD3 = {
                {1, 2, 3},
                {4, 5, 6},
                {7, 8, 9}
        };
        for (int i = 0; i < nums2.length; i++) {
            System.out.println(nums2[i]);
        }
    }
}
