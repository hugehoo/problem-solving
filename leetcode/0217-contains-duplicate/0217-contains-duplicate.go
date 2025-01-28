package main

import "fmt"

func containsDuplicate(nums []int) bool {
	// Pre-allocate map with capacity to avoid resizing
	sets := make(map[int]bool, len(nums))
	for _, num := range nums {
		if sets[num] {
			return true
		}
		sets[num] = true
	}
	return false
}

func main() {
	fmt.Println(containsDuplicate([]int{1, 2, 3, 1}))
	fmt.Println(containsDuplicate([]int{2, 3, 1}))
}