public class Akerman {


  public static int ackermann(int m, int n) {
    if (m == 0) {
      return n + 1;
    } 
	else if (n == 0) {
      return ackermann(m - 1, 1);
    } 
	else {
      return ackermann(m - 1, ackermann(m, n - 1));
    }
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
