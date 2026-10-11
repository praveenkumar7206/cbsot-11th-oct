package lec3_1sep;

public class pattern25 {
    public static void main(String[] args) {
        int n = 5;
        int row = 1;
        int space = 4;
        int star = 1;
        int value = 1;

        while (row<=n){
            int i = 1;
            while (i<=space){
                System.out.print("\t");
                i++;
            }

            int j = 1;
            while(j<=star){
                System.out.print(value+"\t");
                j++;
                value++;
            }

        row++;
        space--;
        star=star+2;
        System.out.println();    



}
        
    }
    
}
