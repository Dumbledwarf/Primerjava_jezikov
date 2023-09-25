package main

import (
    "fmt"
    "time"
)

func ackermann(m, n int) int {

	if m == 0 {
		return n + 1
	}  else if n == 0 {
		return ackermann(m - 1, 1)
	}  else{
		return ackermann(m - 1, ackermann(m, n - 1))
	}
}


func main() {
	startTime := time.Now()
	out := ackermann(4, 1)
	endTime := time.Now()
    timeTaken := endTime.Sub(startTime).Milliseconds()
    fmt.Printf("Time taken: %d milliseconds\n", timeTaken)
	fmt.Printf("Result: %d\n", out)
}
