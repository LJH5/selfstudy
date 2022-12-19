package abs;

public class VehicleTest {

	public static void main(String[] args) {
		Vehicle [] vehicles = {new DieselSUV(), new ElectricCar(), new HorseCart()};
		for(Vehicle v: vehicles) {
			v.addFuel();
			v.reportPosition();
		}
//		Vehicle v = new Vehicle();	// 추상 클래스는 객체를 생성할 수 없다
		Vehicle v = new DieselSUV();	// 다형성은 가능 
	}

}
