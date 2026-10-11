package lec3_1sep;

public class pattern31 {
    public static void main(String[] args) {
        int n = 5;
        int row=1;
        int count=5;
       

        while (row<n){
             int num = 5;
            int i = 1;
            while(i<=count){
                if (row+i==6){
                    System.out.print("*");
                }
                else{
                System.out.print(+num);
                }
                i++;
                num--;
                
            }

            row++;
            System.out.println();
        }
    }
    
}
