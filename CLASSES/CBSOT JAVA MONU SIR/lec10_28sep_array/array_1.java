import java.util.*;

public class array_1 {
    public static void main(String[] args) {
       int []arr = new int[5];
        // [] iska matlab data 1 dimensional hai soo yaha arr ka type int ka 1 dimensional array hai
       System.out.println(arr);
       arr[0]=4;
       arr[1]=-14;
       arr[2]=2;
       arr[3]=3;
       arr[4]=4;
       System.out.println(arr[0]);
       System.out.println(arr[1]);
       System.out.println(arr[2]);
       System.out.println(arr[3]);
       System.out.println(arr[4]);
       System.out.println(arr.length);

       for (int n = 0 ; n<arr.length; n++){
        System.out.print(arr[n]+" ");
       }
    }
}