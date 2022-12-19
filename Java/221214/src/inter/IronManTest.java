package inter;

public class IronManTest {
	
	public static void main(String[] args) {
		IronMan iman = new IronMan();
		Object obj = iman;
		// 인터페이스도 하나의 타입 -> 다형성은 가능
		Transformable tf = iman;
	}

}
