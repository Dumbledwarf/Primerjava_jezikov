#include <stdio.h>
#include <sys/time.h>

#define MAX 10000  

int memo1[MAX + 1][MAX + 1] = {0};

int ackermann(int m, int n) {
  if (m <= MAX && n <= MAX && memo1[m][n] != 0) {
    return memo1[m][n];
  }
  
  int result;
  
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
    memo1[m][n] = result;
  }
  
  
  return result;
}

int main() {
	clock_t start, end;
	double cpu_time_used;
	start = clock(); 
	int out = ackermann(4, 1);
	end = clock(); 
	cpu_time_used = ((double) (end - start) * 1000.0) / CLOCKS_PER_SEC;
	printf("Time taken: %f miliseconds\n", cpu_time_used);
	printf("Result: %d\n", out);
  return 0;
}
