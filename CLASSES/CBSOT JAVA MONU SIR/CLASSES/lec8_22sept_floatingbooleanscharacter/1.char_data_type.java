package lec8_22sept_floatingbooleanscharacter;

public class 1.char_data_type {
      public static void main(String[] args) {

        char ch = 'a';
        System.out.println((int)(ch));
        System.out.println(ch++); // ch = (char)(ch+1);
        System.out.println(ch);
        // ch = ch +1 , yaha error dega hama fir ch = (char)(ch+1); asaq likhna hoga k\yu ki , ch+=1 yaha implicit type catsing khud kar deta hai but ch = ch +1 ma forcefully implicit type casting nhi hota soo hama ch = (char)(ch+1); asa likhna padta hai 
// input of characters
         Scanner sc = new Scanner(System.in);
        ch = sc.next().charAt(0);
      }
    
}
