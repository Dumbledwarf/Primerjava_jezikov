public class Dakerman {
	public static final int MAX = 10000;
    public static int[][] mem = new int[MAX+1][MAX+1];

  public static int ackermann(int m, int n) {
	  if (m <= MAX && n <= MAX && mem[m][n] != 0) {
			return mem[m][n];
		}
		
	int result = 0;
	
    if (m == 0) {
      result = n + 1;
    } 
	else if (n == 0) {
      result = ackermann(m - 1, 1);
    } 
	else {
      result = ackermann(m - 1, ackermann(m, n - 1));
    }
	
	if (m <= MAX && n <= MAX) {
		mem[m][n] = result;
	}
  
	return result;
  }

  public static void main(String[] args) {
	long startTime = System.nanoTime();
    int out = ackermann(4, 1);
	long endTime = System.nanoTime();
    double timeTaken = (endTime - startTime) / 1E6;

    System.out.println("Time taken: " + timeTaken + " milliseconds");
	System.out.println("Result: "+out+"\n");
  }
}
