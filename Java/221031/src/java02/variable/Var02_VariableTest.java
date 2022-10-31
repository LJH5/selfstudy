package java02.variable;

public class Var02_VariableTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		byte a = 20;
		byte b = 10;
		byte c = a + b; // 산술연산의 최소단위는 int, 암시적 형변환(byte -> int)
		
		int i = 10;
		long l = 20;
		int k = i + l; // int + long에서  더 긴 long으로 암시적 형변환
		
		float f1 = 10.0; // 실수의 기본 타입은 double
		float f3 = f1 + 10.0; // 실수의 기본 타입은 double
		float f2 = 10.0f;
	}

}
 