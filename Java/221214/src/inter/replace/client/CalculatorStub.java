package inter.replace.client;

import inter.replace.Calculator;

public class CalculatorStub implements Calculator {

	@Override
	public int add(int a, int b) {
		System.out.printf("파라미터 확인: %d, %d%n", a, b);
		return 0;
	}

}
