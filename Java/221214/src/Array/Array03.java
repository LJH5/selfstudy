package Array;
import java.util.Arrays;

public class Array03 {

	public static void main(String[] args) {
		String org = "1234567890";
		// char 숫자는 빼기 연산이 가능하다
		char [] nums = org.toCharArray();
		int sum = 0;
		for(int i = 0; i < nums.length; i++) {
			sum += nums[i] - '0';
		}
		
		System.out.printf("sum: %d%n", sum);
	}

}
