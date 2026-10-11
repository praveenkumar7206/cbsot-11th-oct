package lec3_1sep;

public class pattern16 {
    public static void main(String[] args) {
        int n = 5; 
          int row = 1;
            int star = 5;
       int space = 4;
    while (row <=2*n-1){

        int j = 1;
        while (j<=space){
            System.out.print("  ");
            j++;
        }
    

        int i= 1;
        while (i<=star){
            System.out.print("* ");
            i++;
        }

         
        
        if (row<n){
            star--;
            space--;
        }
        else{
            star++;
            space++;
        }
    // next row ki prep
    row++;
    System.out.println();
    }
    }
    
}
