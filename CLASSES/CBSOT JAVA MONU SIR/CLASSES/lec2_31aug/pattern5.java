package lec_2_31_aug;

public class pattern5 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int n = 5;
		int row = 1;
		int star = 5;
		int space = 0;
		while(row<=n) {
			
			int j = 1;
			while(j<=space) {
			 System.out.print(" ");
			 j++;
			}
			
			int i =1;
			while (i<=star) {
				System.out.print("* ");
				i++;
			}			
			row++;
			space++;
			star--;
			System.out.println();
			
			
		}

	}

}
