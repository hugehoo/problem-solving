package main

import (
	"fmt"
)


func missingNumber(nums []int) int {
	N := len(nums)
	maps := make(map[int]int)
	for i := 0; i <= N; i++ {
		maps[i] = 1
	}
	
	return 0     
}

func main() {
	fmt.Println(missingNumber([]int {3, 0, 1}))
}