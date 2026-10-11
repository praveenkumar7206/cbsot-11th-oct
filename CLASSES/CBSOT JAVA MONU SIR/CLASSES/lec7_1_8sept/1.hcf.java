package lec7_8sept;

public class hcf {
    public static void main(String[] args) {
        int a= 60;
        int b = 36;

        while(a%b!=0){
            int c = a%b;
            a = b;
            b  =c;
        }
        System.out.println("b");
    }
}