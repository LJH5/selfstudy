package person;

public class SpiderManTest {

	@SuppressWarnings({"deprecation", "unused"})
	public static void main(String[] args) {
		int i = 10;
		SpiderMan sman = new SpiderMan("피터 파커", false);
		
		sman.eat(); // Person
		sman.jump(); // Person
		sman.fireWeb(); // SpiderMan
		
		System.out.println("---스파이더맨으로 변신---");
		sman.isSpider = true;
		sman.eat(); // Person
//		sman.jump(); // Person
		sman.jump(); // Spider 메소드 오버라이딩
		sman.fireWeb(); // SpiderMan
		sman.love();
		System.out.println(sman.toString());
		
		
	}

}
