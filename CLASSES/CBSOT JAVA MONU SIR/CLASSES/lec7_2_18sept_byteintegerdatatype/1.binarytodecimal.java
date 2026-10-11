package lec7_2_18sept;

public class binarytodecimal {
    public static void main(String[] args) {
      int n = 10000000;
      int mul = 1;
      int sum = 0;
      while(n>0){
        int rem = n%10;
        sum = sum + rem*mul;
        mul = mul*2;
        n = n/10;
      }
      System.out.println(sum);
    }
}



