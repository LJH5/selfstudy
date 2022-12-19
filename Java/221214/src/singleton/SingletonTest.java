package singleton;

class SingletonClass {
	// 3. sc를 static으로 만들기
	private static SingletonClass sc =new SingletonClass();
	private SingletonClass() {}
	
	// 1. 생성자가 private라서 객체를 만들지 못하니까 static 사용해서 메모리에 올리기
	public static SingletonClass getSc() {
		// 2. static 에서 nonStatic한 것으로 바로 접근 못함
		return sc;
	}

	public void sayHello() {
		System.out.println("Hello");
	} 
}

public class SingletonTest {

	public static void main(String[] args) {
//		SingletonClass sc1 = new SingletonClass();
		SingletonClass sc1 = SingletonClass.getSc();
		sc1.sayHello();
		SingletonClass sc2 = SingletonClass.getSc();
		sc2.sayHello();
		System.out.println(sc1 == sc2); // 생성된 객체는 단 하나
	}

}
