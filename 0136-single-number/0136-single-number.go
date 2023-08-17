
func singleNumber(nums []int) int {
	counts := make(map[int]int)

	// count the number of occurrences of each digit
	for _, num := range nums {
		counts[num]++
	}

	// find the digit that appears only once
	for num, count := range counts {
		if count == 1 {
			return num
		}
	}

	// if there is no unique digit, return -1 or an error message
	return -1
}