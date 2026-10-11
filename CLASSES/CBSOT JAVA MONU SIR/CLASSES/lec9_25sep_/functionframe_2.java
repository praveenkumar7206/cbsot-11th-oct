package lec9_25sep_;

public class functionframe_2 {
    public static void main(String[] args) {
        System.out.println("hii");
        int a = 8;
        int b = 7;
        sum(b, a); // hamesha call pa variable pass nhi hota uski value pass hoti hai , int a ma 7
                   // value pass hogi
        System.out.println("bye");
    }

    public static void sum(int a, int b) { // iss curly bracker ke andar jo bhi rahgea wo uska anadar hi rahega
        int c = a + b;
        System.out.println(c);
    }

}
