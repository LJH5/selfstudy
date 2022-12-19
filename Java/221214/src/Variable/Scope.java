package Variable;


class Parent{
	public Parent() {
		System.out.println("부모 기본 생성자");
		System.out.println("변수 선언문 위에 " + y);
	}
	String x = "parent";	
	static String y = "부모";
	
}

class Child extends Parent{
	
	public Child() {
		System.out.println("자식 기본 생성자");
		System.out.println("변수 선언문 위에 " + y);
	}
	String x = "child";
	static String y = "자식";
	
	void method() {
		String x = "method";
		System.out.println("x: " + x);
		System.out.println("this.x: " + this.x);
		System.out.println("super.x: " + super.x);
	}
	void A(String x) {
		String y = "A";
		
		System.out.println(x);
		x = this.x;
		System.out.println(x);
		x = super.x;
		System.out.println(x);
		
		System.out.println("================");
		System.out.println(y);
		System.out.println(this.y);
		System.out.println(super.y);
	}
}

public class Scope {
	
	static String y = "여기다";
	
	public static void main(String[] args) {
		Child child = new Child();	// 생성자 호출
		child.method();
		System.out.println("--------------");
		String x = "뭔지";
		child.A(x);
	}

}
