package main

import (
	"fmt"
	"os"
	"math/rand"
)

func main() {
	// Name of the file to write the random numbers
	fileName := "integers.txt"

	// Create or open the file for writing
	file, err := os.Create(fileName)
	if err != nil {
		fmt.Println("Error creating file:", err)
		return
	}
	defer file.Close()

	// Generate 10,000 random numbers within the range of math.MinInt64 and math.MaxInt64 into the file
	for i := 0; i < 10000000; i++ {
		randomNum := generateRandomInt(-20,50)
		_, err := fmt.Fprintf(file, "%d\n", randomNum)
		if err != nil {
			fmt.Println("Error writing to file:", err)
			return
		}
	}

	fmt.Println("Successfully wrote 10,000 random integers into", fileName)
}

// generateRandomInt64 generates a random int64 number in the given range [min, max]
func generateRandomInt(min, max int) int {
	return rand.Intn(max-min+1) + min
}
