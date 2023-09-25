package main

import (
    "fmt"
    "time"
	"math"
	"io/ioutil"
)

func lcs(X, Y string) string {
  m := len(X)
  n := len(Y)

  L := make([][]int, m + 1)
  for i := 0; i <= m; i++ {
    L[i] = make([]int, n + 1)
  }

  for i := 0; i <= m; i++ {
    for j := 0; j <= n; j++ {
      if i == 0 || j == 0 {
        L[i][j] = 0
      } else if X[i - 1] == Y[j - 1] {
        L[i][j] = L[i - 1][j - 1] + 1
      } else {
        L[i][j] = int(math.Max(float64(L[i - 1][j]), float64(L[i][j - 1])))
      }
    }
  }

  lcsLength := L[m][n]
  lcs := make([]byte, lcsLength + 1)
  lcs[lcsLength] = '\x00'

  i := m
  j := n
  for i > 0 && j > 0 {
    if X[i - 1] == Y[j - 1] {
		lcsLength--
      lcs[lcsLength] = X[i - 1]
      i--
      j--
    } else if L[i - 1][j] > L[i][j - 1] {
      i--
    } else {
      j--
    }
  }

  return string(lcs)
}

func readFile(filePath string) (string) {
	fileContents, _ := ioutil.ReadFile(filePath)
	return string(fileContents)
}

func main() {
  X := readFile("string1.txt")
  Y := readFile("string2.txt")
  startTime := time.Now()
  lcs := lcs(X, Y)
  endTime := time.Now()
  timeTaken := endTime.Sub(startTime).Milliseconds()
  fmt.Println(lcs)
  fmt.Println("Time taken: %d milliseconds\n", timeTaken)
}
