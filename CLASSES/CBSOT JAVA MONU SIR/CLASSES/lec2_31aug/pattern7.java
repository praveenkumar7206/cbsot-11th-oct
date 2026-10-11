public class pattern7 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int n = 5;
		int row = 1;
		int star = 5;
		int space =3;
		int star1=1;
		
		while(row<=n) {
			if (row==1 || row==n){
				int i = 1;
                while (i<=star){
					System.out.print("* ");
					i++;
				}
			}
			else{
			int j = 1;
			while(j<=star1){
				System.out.print("* ");
				j++;
			}
			int k = 1;
			while(k<=space){
				System.out.print("  ");
				k++;
			}
			int l = 1;
			while(l<=star1){
				System.out.print("* ");
				l++;
			}
		}


			row++;
			System.out.println();
		}
		

	}

}
