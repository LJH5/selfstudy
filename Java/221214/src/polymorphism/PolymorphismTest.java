package polymorphism;

import person.Person;
import person.SpiderMan;

public class PolymorphismTest {

	public static void main(String[] args) {
		SpiderMan sman = new SpiderMan("피터파커", true);
		// 다형성
		// 묵시적 형변환
		SpiderMan sman2 = sman;
		Person person = sman;
		Object obj = person;
		
		// 명시적 형변환
		SpiderMan reSpider = (SpiderMan)obj;
		reSpider.fireWeb();
		
		// 뭐든지 담을 수 있는 만능의 주머니
		Object [] objs = new Object[4];
		objs[0] = sman;
		objs[1] = "Hello";
		objs[2] = objs;
		objs[3] = 1; // 기본형 -> autoboxing, intger로 wrapping
		
		// 명시적 형변환
		SpiderMan fromObjArray = (SpiderMan)objs[0];
		fromObjArray.fireWeb();
		
		// 형변환을 할 때는 반드시 타입을 확인하고 가자
		if(objs[1] instanceof SpiderMan) {
			SpiderMan fromObjArray2 = (SpiderMan)objs[1];
			fromObjArray.fireWeb();			
		}
		
		for(Object o: objs) {
			System.out.println(o.getClass().getName());
		}
		
		System.out.println(sman2);
	}

}
