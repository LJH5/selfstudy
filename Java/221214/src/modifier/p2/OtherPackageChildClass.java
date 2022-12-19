package modifier.p2;

import modifier.p1.Parent;

public class OtherPackageChildClass extends Parent {
	private void method() {
		this.publicVar = 10;
		this.protectedVar = 10;
//		this.defaultVar = 10;
//		this.privateVar = 10;
	}
}
