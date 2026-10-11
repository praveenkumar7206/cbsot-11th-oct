
// using infifnity for finding maxm
import java.util.*;

public class arrmaxminfinity {
  public static void main(String[] args) {
    int[] arr = { 3, 2, 1, 2, 3, 4, 4, 4, 5, 55, 76, 43 };

    System.out.println(max(arr));
  }

  public static int max(int[] arr) {
    int max = Integer.MIN_VALUE; // - 2^31 , YS ISKI MINM VALUE HOGI , INTEGER KE MINM VALUE , APNA HISABSE LONG
                                 // BHI KAR SAKTA HOO
    for (int i = 1; i < arr.length; i++) {
      if (arr[i] > max) {
        max = arr[i];
      }
    }
    return max;
  }
}