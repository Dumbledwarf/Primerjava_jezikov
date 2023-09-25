import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Matrix {
	static final int DIM = 500;
	
	public static void readNumbers(String filename, long[][] arr) {
        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            for (int i = 0; i < DIM; i++) {
                for (int j = 0; j < DIM; j++) {
					String line = br.readLine();
                    arr[i][j] = Long.parseLong(line);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
	
    public static void mnozenjeMatrik(long[][] A, long[][] C) {        
        for (int i = 0; i < DIM; i++) {
            for (int j = 0; j < DIM; j++) {
                for (int k = 0; k < DIM; k++) {
                    C[i][j] += A[i][k] * A[k][j];
                }
            }
		}
    }

    public static void main(String[] args) {
        long[][] A = new long[DIM][DIM];
		long[][] C = new long[DIM][DIM];
		readNumbers("numbers.txt",A);
        long startTime = System.nanoTime();
		mnozenjeMatrik(A, C);
        long endTime = System.nanoTime();
		double timeTaken = (endTime-startTime) / 1E6;
		System.out.println("Time taken: "+ timeTaken +" milliseconds");
		System.out.println("Number: "+ C[0][0] );
    }
}
