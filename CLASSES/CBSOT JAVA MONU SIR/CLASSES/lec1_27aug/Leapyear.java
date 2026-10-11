

public class Leapyear {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int y = 2028   ;
		if (y%100==0) {
			if (y%400==0) {
				System.out.println("yes a leap year");
			}
			else {
				System.out.println("not a leap year");
			}
		}
		else {
			if (y%4==0) {
				System.out.println("leap year");
			}
			else {
				System.out.println("not a leap year");
			}
		}
	}
}
