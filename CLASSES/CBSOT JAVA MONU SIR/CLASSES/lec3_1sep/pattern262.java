package lec3_1sep;

public class pattern262 {
    public static void main(String[] args) {
        int n = 5;
        int space= 4;
        int row= 1;
        int count = 1;
        
        while (row<=n){
            int i = 1;
            while(i<=space){
                System.out.print("\t");
                i++;
                
            }
            int j = 1;
            int num = 1;
            while(j<=count){
                System.out.print(+num+"\t");
                j++;
                num++;
            }
            row++;
            count= count+2;
            space--;
            System.out.println();
        }
    }
    
}
