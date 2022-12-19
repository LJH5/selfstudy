package abs;

public class ElectricCar extends Vehicle {
	
	@Override
	public void addFuel() {
		System.out.printf("차종: %s, 연료 주입: %s%n", this.getClass().getSimpleName(), "전기");
	}
}
