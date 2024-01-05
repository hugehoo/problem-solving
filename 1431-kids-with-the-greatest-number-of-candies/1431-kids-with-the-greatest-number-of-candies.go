func kidsWithCandies(candies []int, extraCandies int) []bool {
	var lenCandy int = len(candies)
	//result := [lenCandy]bool{}
	result := make([]bool, lenCandy)

	maxNumber := findMax(candies)
	for idx, val := range candies {
		if val+extraCandies >= maxNumber {
			result[idx] = true
		} else {
			result[idx] = false
		}
	}
	return result
}

func findMax(arr []int) int {
	if len(arr) == 0 {
		// Handle empty array case
		return 0 // or any other appropriate value
	}

	max := arr[0] // Initialize max with the first element of the array

	for _, num := range arr {
		if num > max {
			max = num // Update max if a larger element is found
		}
	}

	return max
}
