package lec9_25sep_;

public class returncontent_3 {
    public static void main(String[] args) {
         System.out.println("hii");
        int a = 8;
        int b = 7;
        sum(b, a); 
        System.out.println("bye");
    }

    public static int sum(int a, int b) { 
        int c = a + b;
        return c ;      // yaha hamna void ka return type chanage kar dia int se soo ab ye c ki int value return karega sum ko jaha se ye frame call hua tha , and then waha pa value return ho jati hai soo apna according use kar sakta hai
    }
    
}
