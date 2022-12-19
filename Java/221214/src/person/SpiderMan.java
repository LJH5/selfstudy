package person;

public class SpiderMan extends Person{
	boolean isSpider;
//	Spider spider; // 변수 선언, 메모리 등록은 x
	Spider spider = new Spider(); // 변수 선언, 메모리에 등록
	
	public SpiderMan(String name, boolean isSpider) {
		super(name);
		this.isSpider = isSpider;
	}
	public void fireWeb() {
//		System.out.println("거미줄 발싸!!"); spider 변수 사용 전
		if(isSpider) {
			// null pointer => null.xx  위에서 spider가 메모리에 등록되지 않음
			spider.fireWeb();
		}else {
			System.out.println("사람일때는 참자");
		}
	}
	
	@Override
//	void jumo()시 부모에게 jumo가 없기 때문에 overriding 실패라고 알려줌
	public void jump() {
		if(isSpider) {
			spider.jump();
		}else {
//			System.out.println("두 다리로 폴짝"); // 코드 중복 너무 불편하고
			super.jump();
		}
	}
	
	@Deprecated
	public void love() {
		System.out.println("메리제인 사랑해");
	}
	
	// 자식에서 toString 메서드 오버라이드
	@Override
	public String toString() {
//		return "name: " + this.name + ", isSpider: " + this.isSpider; // name이 중복 정의됨
		return super.toString() + ", isSpider: " + this.isSpider; //super를 사용
	}
	
}
