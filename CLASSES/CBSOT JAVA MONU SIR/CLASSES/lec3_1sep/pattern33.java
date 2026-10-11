import java.util.*;

public class  {
    public static void main(String[] args) {
      int n = 10 ;
      int row = 1;
      int space = 9;
       int num = 9;
     
      int count = 0;
    

      while(row<=n){
        int i = 1;
        while(i<=space){
          System.out.print(" ");
          i++;
        }

        int k = 1;
        
        while(k<=count){
          System.out.print(num+"");
          k++;
          num++;
        }
        System.out.print("0");

        int l = 1;
        int num1=9;
        while(l<=count){
          System.out.print(num1+"");
          l++;
          num1--;
        }
        if (row>1){
          num=num-(count+1);
        }
        row++;
        space--;
        count++;
        System.out.println();

      }
    }
}