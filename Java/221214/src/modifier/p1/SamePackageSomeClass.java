package modifier.p1;

public class SamePackageSomeClass {
	private void method() {
		Parent p = new Parent();
		p.publicVar = 10;
		p.protectedVar = 10;
		p.defaultVar = 10;
//		p.privateVar = 10;
	}
}
