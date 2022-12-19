package inter.module;

public class LaserPrinter implements Printer{

	@Override
	public void print(String fileName) {
		System.out.println("Laser Printer: " + fileName);
		
	}

}
