package Array;
import java.util.Arrays;

public class Array06Plus {
	public static void main(String[] args) {
		// 배열의 행의 크기만 정하기
		// 각각의 행은 가상의 공간의 열이 저장된 주소를 저장
		int [][] intArray = new int[4][];
		intArray[0]	= new int[3];
		intArray[1] = new int[2];
		
		for(int [] x : intArray) {
			System.out.println(Arrays.toString(x));
		}
		System.out.println("---------------------");
		int[] arr = new int [4];
		intArray[2] = arr;
		intArray[2][1] = 10;
		// intArray 2행에는 arr의 주소가 저장
		System.out.println("arr: " + Arrays.toString(arr));
		
		
	}
}
