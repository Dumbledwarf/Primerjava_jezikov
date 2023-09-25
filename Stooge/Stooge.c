#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>
#define ARRAY_SIZE 10000
void stooge_sort(int* arr, int l, int h) {
  if (arr[l] > arr[h]) {
    int temp = arr[l];
    arr[l] = arr[h];
    arr[h] = temp;
  }

  if (h - l + 1 > 2) {
    int t = (h - l + 1) / 3;

    stooge_sort(arr, l, h - t);
    stooge_sort(arr, l + t, h);
    stooge_sort(arr, l, h - t);
  }
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

int main() {
    int* seznam = readNumbersFromFile("numbers.txt");
	clock_t start, end;
	double cpu_time_used;
	start = clock(); 
	stooge_sort(seznam,0,ARRAY_SIZE-1);
	end = clock(); 
	cpu_time_used = ((double) (end - start) * 1000.0) / CLOCKS_PER_SEC;

	printf("Time taken: %f miliseconds\n", cpu_time_used);
    
	free(seznam);

    return 0;
}