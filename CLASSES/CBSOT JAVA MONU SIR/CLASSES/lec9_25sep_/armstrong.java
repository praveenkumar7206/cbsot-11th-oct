
package lec9_25sep_;
import java.util.Scanner;

public class armstrong {
    public static void main(String[] args) {
  Scanner sc = new Scanner(System.in);

  int n = sc.nextInt();
       int cod = count_of_digit(n);
       System.out.println(arm(n,cod));
 
    }

    public static boolean arm(int n , int cod){
    int sum = 0;
    int num = n;
    while(n>0){
        int rem = n%10;
        sum = sum + (int)(Math.pow(rem , cod));
        n = n/10;
    }
    if (sum==num){
        return true;
    }
    else{
        return false;
    }
    }

    public static int count_of_digit(int n) {
        int c = 0;
        while(n>0){
            n = n/10;
            c = c+1;
        }
        return c;
        
    }
    
}
