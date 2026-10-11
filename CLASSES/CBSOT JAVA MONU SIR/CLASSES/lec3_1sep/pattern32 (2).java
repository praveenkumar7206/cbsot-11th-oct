import java.util.*;

public class Main {
    public static void main(String[] args) {
      int n = 5;
      int row = 1;
      int count = 1;
      int num = 1;
      while(row<=2*n-1){
        int i = 1;

        while (i<=count){
          if (i%2==0){
            System.out.print("*");
          }
          else{
            System.out.print(+num);
          } 
          i++;
        }

        if (row<n){
          num++;
          count=count+2;
        }
        else{
          num--;
          count=count-2;
        }
          row++;
          
          System.out.println();
          
        }
      }
}