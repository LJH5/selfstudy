package person;

public class Person {
	public String name = "피터파커";
	
	public Person() {}
	public Person(String name) {
		this.name = name;
	}
	public void eat() {
		System.out.println("냠냠");
	}
	
	public void jump() {
		System.out.println("두 다리로 폴짝");
	}
	// 조상 클래스에서 toString 메서드 오버라이딩
	public String toString() {
        return "person:, name: " + this.name;
    }
}
