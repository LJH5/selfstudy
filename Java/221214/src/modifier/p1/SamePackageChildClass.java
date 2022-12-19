package modifier.p1;

public class SamePackageChildClass extends Parent{
	
	private void method() {
		this.publicVar = 10;
		this.protectedVar = 10;
		this.defaultVar = 10;
//		this.privateVar = 10;
	}
}
