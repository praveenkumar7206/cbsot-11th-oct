package lec3_1sep;

public class pattern12 {
       public static void main(String[] args) {
        int n = 5;
        int row = 1;
        int space = 4;
        int star = 1;

        while (row<=n){
            int i = 1;
            while (i<=space){
                System.out.print(" ");
                i++;
            }

            int j = 1;
            while (j<=star){
            if (j%2!=0){
                System.out.print("*");
            }
            else {
            System.out.print("!");
            

              }
              j++;
            }

        row++;
        space--;
        star+=2;
        System.out.println(); 
        }   

       }
}
