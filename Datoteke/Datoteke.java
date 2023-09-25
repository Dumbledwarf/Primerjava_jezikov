import java.io.FileWriter;
import java.io.IOException;
public class Datoteke {

	public static void datoteke(String text, String file) throws IOException{

		for (int i = 0; i < 100000; i++) {
			FileWriter writer = new FileWriter(file, true);
			writer.write(text);
			writer.close();
		}
		
	}

  public static void main(String[] args) throws IOException {
    long startTime = System.nanoTime();
	datoteke("To je besedilo, ki ga bomo zapisali v datoteko.\n","izhod.txt");
	long endTime = System.nanoTime();
	double timeTaken = (endTime-startTime) / 1E6;
	System.out.println("Time taken: "+ timeTaken +" milliseconds\n");
	}
}