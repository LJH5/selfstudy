package inter.staticdefault;

interface Aircon {
	void makeCool(); 
	
	// TODO: 2. 건조 기능을 추가
//	void dry(); 추상 메소드로 만들경우 Aircon을 implements한 모든 클래스에서 dry()를 오버라이드 해줘야함
	default void dry() {
		System.out.println("에어컨 건조");
	}
	// TODO: 3. Aircon의 동작 방식에 대해 설명해보자
	static void howto() {
		System.out.println("냉매를 이용하여 공기를 차갑게 한다");
	}
}

class OldisButGoodies1 implements Aircon {

	@Override
	public void makeCool() {
		System.out.println("전체 냉각해줘");
	}
	
}

class OldisButGoodies2 implements Aircon {
	
	@Override
	public void makeCool() {
		System.out.println("집중 냉각해줘");
	}
	
}

// TODO: 1. 무풍 에어컨을 구현해보자.
class Nowind1 implements Aircon {
	@Override
	public void makeCool() {
		System.out.println("무풍 모드 가동");
	}
	
	@Override
	public void dry() {
		System.out.println("종료버튼 클릭하면 건조 후 종료");
	}
}
 
public interface StaticDefaultMethod {
	
	public static void main(String[] args) {
		Aircon.howto();
		
		Aircon [] aircons = {new OldisButGoodies1(), new OldisButGoodies2(), new Nowind1()};
		for(Aircon aircon: aircons) {
			if(aircon == null) {
				continue;
			}
			aircon.makeCool();
			aircon.dry();
		}
		
	}
}
