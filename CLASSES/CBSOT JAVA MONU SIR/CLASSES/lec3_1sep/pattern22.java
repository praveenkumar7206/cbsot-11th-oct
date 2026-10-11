package lec3_1sep;

public class pattern22 {
    public static void main(String[] args) {
        int n = 5;
        int row = 1;
        int space = -1;
        int star1 = 5;
        int star2 = 5;

        while (row<=n){

            int k = 1;
            while(k<=star1){
                System.out.print("* ");
                k++;
            }

            int j = 1;
            while(j<=space){
                System.out.print("  ");
                j++;
            }
            int i = 1;
            if (row==1){
                i=2;
            }
            while(i<=star2){
                System.out.print("* ");
                i++;
            }
            row++;
            star1--;
            star2--;
            space= space+2;
            System.out.println();


        }

    }
}
