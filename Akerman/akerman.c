#include <stdio.h>
#include <sys/time.h>


int ackermann(int m, int n) {
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

int main() {
	clock_t start, end;
	double cpu_time_used;
	start = clock(); 
    int out = ackermann(4,1);
	end = clock(); 
	cpu_time_used = ((double) (end - start) * 1000.0) / CLOCKS_PER_SEC;
	printf("Time taken: %f miliseconds\n", cpu_time_used);
	printf("Result: %d\n", out);
    return 0;
}