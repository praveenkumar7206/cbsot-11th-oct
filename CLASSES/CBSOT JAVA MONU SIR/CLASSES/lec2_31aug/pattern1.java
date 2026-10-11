package lec_2_31_aug;

public class pattern1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int n = 5;//total kitna row honga
		int row = 1;//pehle decide kia kitni rows haiu and then row 1 se start kia
		int star = 5; //yaha pa 1st row ma kitna star hoga wo data yaha aayega
		while(row<=n) {
			//star
			int i =1;
			while (i<=star) {
				System.out.print("* ");
				i++;
				
			}
			// next row ki prep
			row++; //yaha next row ma star print karna ke lia , main while loop ke andar hai
			System.out.println(); // line change karna ke lia ln ke karan next line ma jayega
		}

	}

}
