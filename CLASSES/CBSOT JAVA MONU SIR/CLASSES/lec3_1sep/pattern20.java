package lec3_1sep;

public class pattern20 {
    public static void main(String[] args) {
        int n = 7;
        int row= 1;
        int sp1 = 3;
        int st1=1;
        int sp2= -1;

        while (row<=n){
            int i = 1;
            while (i<=sp1){
                System.out.print(" ");
                i++;
            }
             int j = 1;
            while (j<=st1){
                System.out.print("*");
                j++;
            }
            if (row<7 && row>=2) {
                 int k = 1;
            while (k<=sp2){
                System.out.print(" ");
                k++;
            }
                 int l = 1;
            while (l<=st1){ 
                System.out.print("*");
                l++;
            }
        }
            if (row<(n+1)/2){
                sp1--;
                sp2=sp2+2;
            }
            else{
                sp1++;
                sp2 = sp2-2;
            }    
            
            row++;
            System.out.println();
        }
    }
    
}
