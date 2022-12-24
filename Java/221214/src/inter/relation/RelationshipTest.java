package inter.relation;

public class RelationshipTest {

	public static void main(String[] args) {
		Object [] objs = {new HandPhone(), new Camera(), new Phone(), new DigitalCamera()};
		
		// TODO: 충전 가능한 객체들을 충천하시오.
		for(Object obj: objs) {
			if(obj instanceof Chargeable) {
				Chargeable c = (Chargeable)obj;
				c.charge();
			}
		}
	}

}
