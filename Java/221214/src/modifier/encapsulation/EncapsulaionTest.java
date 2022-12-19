package modifier.encapsulation;

class Encapsulaion {
	// 이름은 null이 될 수 없음
	private String name = "홍길동";
	// 나이는 0이상
	private int age = 20;
	public String getName() {
		return name;
	}
	public void setName(String name) {
		if(name != null) {
			this.name = name;			
		}else {
			System.out.println("이름을 입력하세요!");
		}
	}
	public int getAge() {
		return age;
	}
	public void setAge(int age) {
		if(age >= 0) {
			this.age = age;			
		}else {
			System.out.println("음수 값은 안돼요!");
		}
	}
}

public class EncapsulaionTest {

	public static void main(String[] args) {
		Encapsulaion e = new Encapsulaion();
		System.out.printf("사용자 정보: %s, %d%n", e.getName(), e.getAge());
		
		e.setName(null);
		e.setAge(-10);
		
		e.setName("최고존엄");
		e.setAge(28);
		System.out.printf("사용자 정보: %s, %d%n", e.getName(), e.getAge());
	}

}
