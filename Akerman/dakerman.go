package main

import (
    "fmt"
    "time"
)

const MAX = 10000
var mem1 [MAX+1][MAX+1]int

func ackermann(m, n int) int {
	if m <= MAX && n <= MAX && mem1[m][n] != 0{
		return mem1[m][n]
	} 
	result := 0
	if m == 0 {
		result = n + 1
	}  else if n == 0 {
		result = ackermann(m - 1, 1)
	}  else{
		result = ackermann(m - 1, ackermann(m, n - 1))
	}
	
	if m <= MAX && n <= MAX {
		mem1[m][n] = result
	} 
	
	return result
}


func main() {
	startTime := time.Now()
	out := ackermann(4, 1)
	endTime := time.Now()
    timeTaken := endTime.Sub(startTime).Milliseconds()
    fmt.Printf("Time taken: %d milliseconds\n", timeTaken)
	fmt.Printf("Result: %d\n", out)
}
