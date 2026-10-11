package lec3_1sep;

public class pattern28 {
    public static void main(String[] args) {
        int n = 5;
        int space = 4;
        int row = 1;
        int star = 1;
        int num = 1;

        while(row<=n){
            int i = 1;
            while (i<=space) {
                System.out.print(" ");
                i++;
            }
            int j = 1;
             while(j<=star){
                System.out.print(+num);
             if (j<star/2+1){
                num++;
             }
             else{
                num--;
             }
j++;
            }
             row ++;
             star= star+2;
             space--;
             System.out.println()

        }
    }
    
}
