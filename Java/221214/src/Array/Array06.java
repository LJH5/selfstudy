package Array;
import java.util.Arrays;

public class Array06 {

	public static void main(String[] args) {
		// 2차원 배열 만들기
		int [][] intArray = new int[4][3];;
		// 방법2 int intArray[][] = new int [4][3];
		// 방법3 int [] intArray[] = new int [4][3];
		// 방법 4 int [][] intArray = {{0, 1, 2}, {0, 1, 2}, {0, 1, 2}, {0, 1, 2}};
		// 방법 5 int [][] intArray = new int[][] {{0, 1, 2}, {0, 1, 2}, {0, 1, 2}, {0, 1, 2}};
		
		intArray[0][2] = 2;
		for(int [] x : intArray) {
			System.out.println(Arrays.toString(x));
		}

	}

}
