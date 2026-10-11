package lec3_1sep;

public class pattern13 {
    public static void main(String[] args) {
    int n = 5; 
    int row = 1;
    int star = 1;
    while (row <=2*n-1){
        //star ka print logic

        int i= 1;
        while (i<=star){
            System.out.print("* ");
            i++;
        }

         //mirror ke lia
        if (row<n){
            star++;
        }
        else{
            star--;
        }
    // next row ki prep
    row++;
    System.out.println();
    }
    }
}
