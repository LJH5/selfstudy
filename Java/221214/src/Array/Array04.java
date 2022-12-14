package Array;
import java.util.Arrays;

public class Array04 {
	public static void main(String[] args) {
	int [] b = new int [] {1, 2, 3, 4};
	int [] c = {3, 4, 5, 6};
	
	int [] points;
//	points = {1, 3, 4, 5}; // 컴파일 오류
	
	points = new int [] {1, 3, 4, 5};
	System.out.println(Arrays.toString(points));
	}
}
