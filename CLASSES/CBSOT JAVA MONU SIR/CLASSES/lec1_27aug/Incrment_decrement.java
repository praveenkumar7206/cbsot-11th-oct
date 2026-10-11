package lec_1;

public class Incrment_decrement {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int x = 8;
//		x++; // x = x+1
//		x--; // x = x-1
		System.out.println(x++);  // post increment (sabsa pahla x print hoga and then x ke value 1 se badhegi and then wo badhi hui value x ko assign hogi "9" )
//		System.out.println(--x); // pre decrement ( as it is yaha sabsa pahla -- act karega soo x ki value pahla x-1 ho jayegi then x-1 print hoga )
		 
		int i = ++x - ++x+ --x - --x + x++;
		System.out.println(i);
	}

}
