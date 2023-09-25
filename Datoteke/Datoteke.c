#include <stdio.h>
#include <time.h>

void write_to_file(char* text, char* filename) {
  
  for (int i = 0; i < 100000; i++) {
	FILE* fp = fopen(filename, "a");

	fputs(text, fp);

	fclose(fp);  
  }
}

int main(int argv, char* argc){
	clock_t start, end;
    double cpu_time_used;

    start = clock(); 

    write_to_file("To je besedilo, ki ga bomo zapisali v datoteko.\n","izhod.txt");

    end = clock(); 

    cpu_time_used = ((double) (end - start)*1000.0) / CLOCKS_PER_SEC;

    printf("Time taken: %f miliseconds\n", cpu_time_used);

    return 0;
}