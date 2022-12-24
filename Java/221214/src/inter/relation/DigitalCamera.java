package inter.relation;

public class DigitalCamera extends Camera implements Chargeable{
	// TODO: Chargeable을 구현하시오.
	@Override
	public void charge() {
		System.out.println("디카 충전");
	}
}
