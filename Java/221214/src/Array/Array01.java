package Array;
import java.util.Arrays;
import java.util.Random;

public class Array01 {

	public static void main(String[] args) {
		// 배열은 가상의 공간에 만들고 변수에 그 공간의 주소를 저장
		// 1 ~ 6까지의 random 정수 5개를 저장할 배열
		Random rand = new Random();
		int [] arr = new int [5];
		for(int i=0; i < arr.length; i++) {
			
			arr[i] = rand.nextInt(6) + 1;
		}
		System.out.println(Arrays.toString(arr));
		
		// 위 배열에 저장된 요소 중 짝수만 더해서 합을 출력하시오.
		int sum = 0;
		for(int i=0; i < arr.length; i++) {
			if(arr[i] % 2 == 0) {
				sum += arr[i];
			}
		}
		System.out.println(sum);
	}

}
