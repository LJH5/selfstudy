package inter.relation;

public class HandPhone extends Phone implements Chargeable{

	@Override
	public void charge() {
		System.out.println("핸드폰 충천");
	}

}
