package inter.module;

public class PrinterTest {

	public static void main(String[] args) {
		PrintClient client = new PrintClient();
		client.setPrinter(new DotPrinter());
		client.setPrinter(new LaserPrinter());
		client.printThis("myfile");
	}

}
