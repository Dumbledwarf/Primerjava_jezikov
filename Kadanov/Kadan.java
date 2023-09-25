import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.ArrayList;

public class Kadan {

    public static long[] readFromFile(String file) throws Exception{
		BufferedReader br = new BufferedReader(new FileReader(file));
		String line = null;
		ArrayList<Long> ret = new ArrayList<>();
		while ((line = br.readLine()) != null) {
		  long number = Long.parseLong(line.trim());
		  ret.add(number);
		}
		br.close();
		return ret.stream().mapToLong(i -> i).toArray();
	}
	
  public static	long kadane(long[] arr) {
  long maxEndingHere = 0;
  long maxSoFar = Integer.MIN_VALUE;

  for (int i = 0; i < arr.length; i++) {
    maxEndingHere = maxEndingHere + arr[i];
    if (maxEndingHere < 0) {
      maxEndingHere = 0;
    }
    if (maxSoFar < maxEndingHere) {
      maxSoFar = maxEndingHere;
    }
  }

  return maxSoFar;
}

	public static void main(String[] args) throws Exception{
		long[] seznam = readFromFile("numbers.txt");
		long startTime = System.nanoTime();
		long ret = kadane(seznam);
		long endTime = System.nanoTime();
		double timeTaken = (endTime-startTime) / 1E6;
		System.out.println("Time taken: "+ timeTaken +" milliseconds");
		System.out.println("Result:" + ret +"\n");
	}
}