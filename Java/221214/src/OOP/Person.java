package OOP;
// 클래스: 타입, 붕어빵 틀
public class Person {
	// 클래스 멤버 변수 
	static String org = "Deajeon";
	// 인스턴스 멤버 변수 - 속성, 데이터
	String name;
	int age;
	boolean isHungry;
	
	// 멤버 메서드 - 동작
	void eat() {
		System.out.println("냠냠");
		isHungry = false;
	}
	
	void work() {
		System.out.println("열심히");
		isHungry = true;
	}
}
