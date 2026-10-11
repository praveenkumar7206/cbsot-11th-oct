package lec7_8sept;

public class 4.swapof2number {
    public static void main(String[] args) {
        int a = 10;
        int b = 20;
        // int c = a ; 
        // a = b;
        // b=c;
        // System.out.println(a+" "+b);

        // we have to do without using 3rd variable

          a = a+b;
           b = a-b; // a (30) ma se b(20) soo aayega wo 10 hai and ham 10 ko b ma chahta hai 
          a = a-b;
         System.out.println(a+" "+b);
    }
}
