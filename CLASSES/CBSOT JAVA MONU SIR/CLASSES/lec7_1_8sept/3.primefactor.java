class Main {
    public static void main(String[] args) {
        //fidning prime factor of n
        int n = 378;
        int i = 2;
        while(n>1){
            if (n%i==0){  // checking one by one
                System.out.println(i);
                n=n/i;
            }
            else{
                i++; // increasing if not divides
            }
        }
    }
}
