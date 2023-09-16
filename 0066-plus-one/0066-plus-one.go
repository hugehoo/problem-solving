package main


import (
	"fmt"
	"math/big"
	"strconv"
)

func plusOne(digits []int) []int {
	var result string

	for _, num := range digits {
		result += strconv.Itoa(num)
	}
	d := new(big.Int)
	d.SetString(result, 10)
	resultDigits := new(big.Int).Add(d, big.NewInt(1))

	resultString := resultDigits.String()
	newDigits := make([]int, len(resultString))
	for i, num := range resultString {
		digit, _ := strconv.Atoi(string(num))
		newDigits[i] = digit
	}
	return newDigits
}
