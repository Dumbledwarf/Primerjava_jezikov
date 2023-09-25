import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.ArrayList;

public class Stooge {

    public static void stoogeSort(long[] arr, int l, int h) {
        if (arr[l] > arr[h]) {
            long temp = arr[l];
            arr[l] = arr[h];
            arr[h] = temp;
        }

        if (h - l + 1 > 2) {
            int t = (h - l + 1) / 3;

            stoogeSort(arr, l, h - t);
            stoogeSort(arr, l + t, h);
            stoogeSort(arr, l, h - t);
        }
    }

    public static long[] readFromFile(String file) throws Exception{
		BufferedReader br = new BufferedReader(new FileReader(file));
		String line = null;
		ArrayList<Long> ret = new ArrayList<>();
		
		while ((line = br.readLine()) != null ) {
		  long number = Long.parseLong(line.trim());
		  ret.add(number);
		}
		br.close();
		return ret.stream().mapToLong(i -> i).toArray();
	}

	public static void main(String[] args) throws Exception {

		long[] seznam = readFromFile("numbers.txt");
		long startTime = System.nanoTime();
		stoogeSort(seznam, 0, seznam.length-1);
		long endTime = System.nanoTime();
		double timeTaken = (endTime-startTime) / 1E6;
		System.out.println("Time taken: "+ timeTaken +" milliseconds");

	}
}