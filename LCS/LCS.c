#include <stdio.h>
#include <time.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#define MAX(X, Y) (((X) < (Y)) ? (Y) : (X))

int** L;

char* readFile(const char* file_path) {
	FILE* file;
    char* file_contents;
    long file_size;

    file = fopen(file_path, "r");

    fseek(file, 0, SEEK_END);
    file_size = ftell(file);
    fseek(file, 0, SEEK_SET);
	
	file_size -=1;

    file_contents = (char*)malloc(file_size + 1);

    size_t bytes_read = fread(file_contents, 1, file_size, file);

    file_contents[file_size] = '\0';

    fclose(file);

    return file_contents;
}

char* lcs(char* X, char* Y) {
  int m = strlen(X);
  int n = strlen(Y);

  L = malloc(sizeof(int*) * (m + 1));
  for (int i = 0; i <= m; i++) {
    L[i] = malloc(sizeof(int) * (n + 1));
  }

  for (int i = 0; i <= m; i++) {
    for (int j = 0; j <= n; j++) {
      if (i == 0 || j == 0) {
        L[i][j] = 0;
      } else if (X[i - 1] == Y[j - 1]) {
        L[i][j] = L[i - 1][j - 1] + 1;
      } else {
        L[i][j] = MAX(L[i - 1][j], L[i][j - 1]);
      }
    }
  }

  int lcsLength = L[m][n];
  char* lcs = malloc(sizeof(char) * (lcsLength + 1));
  lcs[lcsLength] = '\0';

  int i = m, j = n;
  while (i > 0 && j > 0) {
    if (X[i - 1] == Y[j - 1]) {
      lcs[--lcsLength] = X[i - 1];
      i--;
      j--;
    } else if (L[i - 1][j] > L[i][j - 1]) {
      i--;
    } else {
      j--;
    }
  }

  free(L);
  return lcs;
}

int main() {
  char* X = readFile("string1.txt");
  char* Y = readFile("string2.txt");
  clock_t start, end;
	double cpu_time_used;

	start = clock(); 

	char* lcsSeq = lcs(X, Y); 

	end = clock();

	cpu_time_used = ((double) (end - start)*1000.0) / CLOCKS_PER_SEC;
	printf("%s\n",lcsSeq);
	printf("Time taken: %f miliseconds\n", cpu_time_used);
	free(lcsSeq);
  return 0;
}
