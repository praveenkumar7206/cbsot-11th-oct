package lec3_1sep;

public class pattern272 {
    public static void main(String[] args) {
        int n = 5;
        int row = 1;
        int space = 4;
        int count = 1;
        
         while (row<=n){
            int i = 1;
            while (i<=space) {
                System.out.print("\t");
                i++;
            }
            int j = 1;
            int num = 1;
            while (j<=count) {
                System.out.print(+num+"\t");
            
            if (j<count/2+1){
                num++;
            }
            else{
                num--; 
            }
            j++;
        }
            row++;
            space--;
            count = count+2;
            System.out.println();
         }
    }
    
}
