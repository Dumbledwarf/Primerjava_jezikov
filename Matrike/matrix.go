package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"time"
)

const DIM = 500

func readNumbers(filename string, arr* [500][500]int64) {
	file, _ := os.Open(filename)

	defer file.Close()

	scanner := bufio.NewScanner(file)
	for i := 0; i < DIM; i++ {
		for j := 0; j < 500 && scanner.Scan(); j++ {
			num, err := strconv.ParseInt(scanner.Text(), 10, 64)
			if err != nil {
				continue
			}
			arr[i][j] = num
		}
	}
}


func mnozenjeMatrik(A *[500][500]int64, C *[500][500]int64) {
    for i := 0; i < DIM; i++ {
        for j := 0; j < DIM; j++ {
            for k := 0; k < DIM; k++ {
                C[i][j] += A[i][k] * A[k][j]
            }
        }
    }
}

func main() {
    var A[DIM][DIM]int64
	var C[DIM][DIM]int64
	readNumbers("numbers.txt",&A)
    startTime := time.Now()
	mnozenjeMatrik(&A,&C)
	endTime := time.Now()
    timeTaken := endTime.Sub(startTime).Milliseconds()
    fmt.Printf("Time taken: %d milliseconds\n", timeTaken)
	fmt.Printf("Number: %d\n",C[0][0])
}
