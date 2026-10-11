package lec9_25sep_;

public class functionframe_1 {
    public static void main(String[] args) {
             System.out.println("hii");
        sum();
        System.out.println("bye");    
    }
    public static void sum() {  // iss curly bracker ke andar jo bhi rahgea wo uska anadar hi rahega 
        int a = 8;
        int b = 7;
        int c =a+b;
        sub();
        System.out.println(c);
    }
     public static void sub() {
        int a = 8;
        int b = 7;
        int c =a-b;
        System.out.println(c);
    }
    
}
