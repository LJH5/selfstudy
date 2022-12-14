package Array;

public class Array05 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int intArray [] = {1, 3, 5, 7, 9};
		
		for(int x : intArray) {
			System.out.println(x);
		}
		System.out.println("---------------");
		
		String[] students = {"홍길동", "임꺽정", "장길산", "이몽룡"};
		
		for (String student : students) {
			System.out.println(student);
		}
		System.out.println("---------------");
		
		// 스왑
		String temp = students[1];
		students[1] = students[2];
		students[2] = temp;
		
		for (String student : students) {
			System.out.println(student);
		}
	}

}

