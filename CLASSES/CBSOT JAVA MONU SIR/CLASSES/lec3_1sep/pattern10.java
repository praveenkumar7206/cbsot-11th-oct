package lec3_1sep;

public class pattern10 {
    public static void main(String[] args) {
        int n = 5;
        int row = 1;
        int space = 0;
        int star = 9;

        while (row<=n){
            int i = 1;
            while (i<=space){
                System.out.print("  ");
                i++;
            }

            int j = 1;
            while(j<=star){
                System.out.print("* ");
                j++;
            }

        row++;
        space++;
        star=star-2;
        System.out.println();  
        }  

    }
}
