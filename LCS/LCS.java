import java.util.Arrays;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class LCS {

  public static String lcs(String X, String Y) {
    int m = X.length();
    int n = Y.length();

    int[][] L = new int[m + 1][n + 1];
    for (int i = 0; i <= m; i++) {
      Arrays.fill(L[i], 0);
    }

    for (int i = 1; i <= m; i++) {
      for (int j = 1; j <= n; j++) {
        if (X.charAt(i - 1) == Y.charAt(j - 1)) {
          L[i][j] = L[i - 1][j - 1] + 1;
        } else {
          L[i][j] = Math.max(L[i - 1][j], L[i][j - 1]);
        }
      }
    }

    int lcsLength = L[m][n];
    char[] lcs = new char[lcsLength + 1];
    lcs[lcsLength] = '\0';

    int i = m, j = n;
    while (i > 0 && j > 0) {
      if (X.charAt(i - 1) == Y.charAt(j - 1)) {
		  lcsLength -= 1;
        lcs[lcsLength] = X.charAt(i - 1);
        i--;
        j--;
      } else if (L[i - 1][j] > L[i][j - 1]) {
        i--;
      } else {
        j--;
      }
    }

    return new String(lcs);
  }
	
	public static String readFile(String filePath) throws IOException {
        Path path = Paths.get(filePath);
        byte[] bytes = Files.readAllBytes(path);
        return new String(bytes, StandardCharsets.UTF_8);
    }
	
  public static void main(String[] args) throws IOException{
    String X = readFile("string1.txt");
    String Y = readFile("string2.txt");
	long startTime = System.nanoTime();
    String lcs = lcs(X, Y);
	long endTime = System.nanoTime();
	double timeTaken = (endTime-startTime) / 1E6;
	System.out.println("Time taken: "+ timeTaken +" milliseconds");
    System.out.println(lcs);
  }
}
