package lec3_1sep;

public class pattern242 {
    public static void main(String[] args) {
        int n = 5;
        int space = 4;
        int count = 1;
        int row = 1;
        int num = 1;

        while(row<=n){
            int i = 1;
            while(i<=space){
            System.out.print(" ");
            i++;
        }
        int j = 1;
        while(j<=count){
            System.out.print(+num);
            j++;
        }
        row++;
        count= count+2;
        num++;
        space--;
        System.out.println();
    }
    }
    
}
