package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"time"
	"io"
)

func readNumbersFromFile(filename string) ([]int, error) {
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
	return numbers, nil
}

func stoogeSort(arr []int, l int, h int) {
  if arr[l] > arr[h] {
    temp := arr[l]
    arr[l] = arr[h]
    arr[h] = temp
  }

  if h - l + 1 > 2 {
    t := (h - l + 1) / 3

    stoogeSort(arr, l, h - t)
    stoogeSort(arr, l+t, h)
    stoogeSort(arr, l, h - t)
  }
}

func main() {
	seznam, _ := readNumbersFromFile("numbers.txt")

	startTime := time.Now()
	stoogeSort(seznam,0,len(seznam)-1)
	endTime := time.Now()
    timeTaken := endTime.Sub(startTime).Milliseconds()
    fmt.Printf("Time taken: %d milliseconds\n", timeTaken)
}