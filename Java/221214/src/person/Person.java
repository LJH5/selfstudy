package person;

public class Person {
	String name = "피터파커";
	
	void eat() {
		System.out.println("냠냠");
	}
	
	void jump() {
		System.out.println("두 다리로 폴짝");
	}
	// 조상 클래스에서 toString 메서드 오버라이딩
	public String toString() {
        return "person:, name: " + this.name;
    }
}
