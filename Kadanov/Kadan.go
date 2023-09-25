package main

import (
    "fmt"
    "time"
	"bufio"
	"os"
	"strconv"
	"io"
	"math"
)

func kadane(arr []int) int {
  maxEndingHere := 0
  maxSoFar := math.MinInt32

  for i := 0; i < len(arr); i++ {
    maxEndingHere = maxEndingHere + arr[i]
    if maxEndingHere < 0 {
      maxEndingHere = 0
    }
    if maxSoFar < maxEndingHere {
      maxSoFar = maxEndingHere
    }
  }

  return maxSoFar
}

func readNumbersFromFile(filename string) ([]int) {
	file, _ := os.Open(filename)

	defer file.Close()

	var numbers []int

	reader := bufio.NewReader(file)
	for {
		line, _ , err:= reader.ReadLine()
		if err == io.EOF {
			break
		}
		num, _ := strconv.Atoi(string(line))
		numbers = append(numbers,num)
	}
	return numbers
}

func main() {
	
  seznam := readNumbersFromFile("numbers.txt")
  startTime := time.Now()
  kadane := kadane(seznam)
  endTime := time.Now()
  timeTaken := endTime.Sub(startTime).Milliseconds()
  fmt.Println(kadane)
  fmt.Println("Time taken: %d milliseconds\n", timeTaken)
}