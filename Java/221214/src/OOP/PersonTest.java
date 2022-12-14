package OOP;

// Person을 사용하는 주체?
public class PersonTest {

	public static void main(String[] args) {
		// 클래스 변수는 클래스로 접근
		Person.org = "Deajeon2";
		
		// 붕어빵 틀(Person) 클래스 -> 붕어빵(p, p2) 객체
		Person p = new Person(); // 클래스의 이름은 타입이 된다
		p.name = "홍길동";
		p.age = 30;
		p.isHungry = true;
		p.eat();
		System.out.println(p.name + " : " + p.isHungry + " : " + p.org);
		
		Person p2 = new Person();
		p2.name = "장길산";
		System.out.println(p2.name + " : " + p2.isHungry + " : " + p2.org);
		p2.work();
		System.out.println(p2.name + " : " + p2.isHungry + " : " + Person.org);
	}

}
