package Java04.control;

public class Loop01 {
	public static void main(String[] args) {
//		for (int i = 0 ; i < 10 ; i+=2) {
//			System.out.println(i);
//		}
//		int i = 0;
//		for (;i<10;) {
//			System.out.println(i);
//			i += 2;
//		}
		
		for (int i = 2; i <= 9; i++) {
			System.out.printf("%d단\n", i);
			for (int j = 1; j <= 9; j++) {
				System.out.printf("%d * %d = %d\n", i, j, i*j);
			}
		}
	}
}
