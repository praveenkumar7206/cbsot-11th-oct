import java.util.*;

public class array_selfinput_3 {
    public static void main(String[] args) {
        int[] arr = { 10, 20, 30, 7, 9 };
    }

    int[] arr1 = new int[] { 10, 20, 30, 6, 5, };

    // yaha hamloh square bracket vairable ke baad bhi laga sakt hai
    System.out.println(arr[0]+" "+arr[1]);

    swap(arr[0] , arr[1]);
            System.out.println(arr[0]+ " " + arr[1]);

    public static void swap(int a, int b) {
        int temp = a;
        a = b;
        b = temp;
    }0

}