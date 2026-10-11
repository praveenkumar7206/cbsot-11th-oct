package lec3_1sep;

public class pattern21 {
    public static void main(String[] args) {
        int n = 5;
        int row = 1;
        int star1 = 1;
        int space = 7;
        int star2 = 1;

        while (row<=n){

            int i = 1;
            while (i<=star1){
                System.out.print("* ");
                i++;
            }
            int j = 1;
            while (j<=space){
                System.out.print("  ");
                j++;
            }
            int k = 1;
            if (row==n){
                k=2;
                 }
            while (k<=star2){
                System.out.print("* ");
                k++;
                }
                
            
        row++;
        star1++;
        space= space-2;
        star2++;
        System.out.println() ; 
        }
        
    }
}
