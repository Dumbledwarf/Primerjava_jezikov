package main

import (
    "fmt"
    "time"
	"os"
)

func writeToFile(text, filename string) {
  for i := 0; i < 100000; i++ {
	 os.WriteFile(filename, []byte(text), 0644)
  }
}

func main() {
  startTime := time.Now()
  writeToFile("To je besedilo, ki ga bomo zapisali v datoteko.\n", "izhod.txt")
  endTime := time.Now()
  timeTaken := endTime.Sub(startTime).Milliseconds()
  fmt.Printf("Time taken: %d milliseconds\n", timeTaken)
}