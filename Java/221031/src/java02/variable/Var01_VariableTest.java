package java02.variable;

public class Var01_VariableTest {

	public static void main(String[] args) {
		int a;
		a = 10;
		System.out.println(a); //변수는 값을 할당하지 않고 사용할 수 없다
		
		int b = 20;
		System.out.println(b);
		
		int c = a;
		System.out.println(c);
		c = b;
		System.out.println(c);
		
		System.out.printf("변수 c의 값은 %d", c);
	}

}
