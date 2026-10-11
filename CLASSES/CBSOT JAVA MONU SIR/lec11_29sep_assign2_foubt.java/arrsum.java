public class arrsum {
  public static void main(String[] args) {
    int[] arr = { 3, 2, 1, 2, 3, 4, 4, 4, 5, 55, 76, 43 };

    System.out.println(sum(arr));
  }
  public static int sum(int[] arr){
    int sum = 0;
    for (int i = 0 ; i<=arr.length ; i++){
        sum = sum+ arr[i];
    }
    return sum ;
  }