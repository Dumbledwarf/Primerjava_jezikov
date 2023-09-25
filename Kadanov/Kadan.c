#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <limits.h>
#include <string.h>

#define ARRAY_SIZE 10000000

int kadane(int* arr, int n) {
  int max_ending_here = 0;
  int max_so_far = INT_MIN;

  for (int i = 0; i < n; i++) {
    max_ending_here = max_ending_here + arr[i];
    if (max_ending_here < 0) {
      max_ending_here = 0;
    }
    if (max_so_far < max_ending_here) {
      max_so_far = max_ending_here;
    }
  }

  return max_so_far;
}

int* readNumbersFromFile(const char* filename) {
    FILE* file = fopen(filename, "r");

    int* numbersArray = (int*)malloc(sizeof(int) * ARRAY_SIZE);

    char buffer[1024];
    int i = 0;

    while (fgets(buffer, sizeof(buffer), file) != NULL && i < ARRAY_SIZE) {
        int number = atoi(buffer);
        numbersArray[i++] = number;
    }

    fclose(file);

    return numbersArray;
}

int main(int argv, char* argc){
	clock_t start, end;
    double cpu_time_used;
	
	int* seznam = readNumbersFromFile("numbers.txt");
	
    start = clock();

    int max = kadane(seznam, ARRAY_SIZE);

    end = clock();

    cpu_time_used = ((double) (end - start)*1000.0) / CLOCKS_PER_SEC;

    printf("Time taken: %f miliseconds\n", cpu_time_used);
	printf("%d\n",max);
    return 0;
}