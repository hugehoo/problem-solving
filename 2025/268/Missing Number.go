package main

import (
	"fmt"
)


func missingNumber(nums []int) int {
	N := len(nums)
	maps := make(map[int]int)
	for _, n := range(nums) {
		maps[n] = 1
	}
	for i := 0; i <= N; i++ {
		if maps[i] != 1 {
			return i
		}
	}
	return N     
}

func main() {
	fmt.Println(missingNumber([]int {3, 0, 1}))
}