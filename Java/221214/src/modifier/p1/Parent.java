package modifier.p1;

public class Parent {
	public int publicVar;
	protected int protectedVar;
	int defaultVar;
	@SuppressWarnings("unused")
	private int privateVar;
	
	private void userMember() {
		this.publicVar = 10;
		this.protectedVar = 10;
		this.defaultVar = 10;
		this.privateVar = 10;
	}
}
