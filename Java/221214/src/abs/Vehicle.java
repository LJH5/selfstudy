package abs;

public abstract class Vehicle {
	private int curX, curY;
	
	public void reportPosition() {
		System.out.printf("차종: %s, 현재 위치: (%d, %d)%n", this.getClass().getSimpleName(), curX, curY);
	}
	
	public abstract void addFuel();
}
