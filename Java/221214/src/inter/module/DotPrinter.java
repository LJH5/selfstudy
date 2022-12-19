package inter.module;

public class DotPrinter implements Printer{

	@Override
	public void print(String fileName) {
		System.out.println("Dot Printer: " + fileName);
	}
	
}
