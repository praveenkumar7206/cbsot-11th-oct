package lec3_1sep;

public class pattern23 {
    public static void main(String[] args) {
        
    
    int n = 5;
    int row=1;
    int one=1;
    int space=4;
    
    while (row<=n){
        int i = 1;
        while(i<=one){
            System.out.print("1");
            i++;
        }
        int j = 1;
        while(j<=space){
            System.out.print(" ");
            j++;
        }
        row++;
        one=one+2;
        space--;
        System.out.println();

    }
    }
    
}
