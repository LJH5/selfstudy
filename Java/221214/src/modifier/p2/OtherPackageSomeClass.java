package modifier.p2;

import modifier.p1.Parent;

public class OtherPackageSomeClass {
	private void mehtod() {
		Parent p = new Parent();
		p.publicVar = 10;
//		p.protectedVar = 10;
//		p.defaultVar = 10;
//		p.privateVar = 10;
	}
}
