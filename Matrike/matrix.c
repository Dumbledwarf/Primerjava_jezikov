#include <time.h>
#include <stdio.h>
#include <stdlib.h>

#define DIM 500

void mnozenjeMatrik(int A[][DIM], int C[][DIM]) { 
    
    for (int i = 0; i < DIM; i++) {
        for (int j = 0; j < DIM; j++) {
            for (int k = 0; k < DIM; k++) {
                C[i][j] += A[i][k] * A[k][j];
            }
        }
    }
}

void readNumbers(char* filename, int arr[][DIM]) {
    FILE* file = fopen(filename, "r");

    for (int i = 0; i < DIM; i++) {
        for (int j = 0; j < DIM; j++) {
            fscanf(file, "%d", &arr[i][j]);
        }
    }

    fclose(file);
}

int main() {
    int A[DIM][DIM],C[DIM][DIM];
    readNumbers("numbers.txt", A);
    
	clock_t start, end;
    double cpu_time_used;
    start = clock(); 
	mnozenjeMatrik(A,C);
    end = clock(); 
    cpu_time_used = ((double) (end - start) * 1000.0) / CLOCKS_PER_SEC;
    printf("Time taken: %f miliseconds\n", cpu_time_used);
	printf("%d\n",C[0][0]);
    return 0;
}
