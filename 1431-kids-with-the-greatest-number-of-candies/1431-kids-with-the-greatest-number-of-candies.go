func kidsWithCandies(candies []int, extraCandies int) []bool {
	var lenCandy = len(candies)
	result := make([]bool, lenCandy)
	maxNumber := 0
	for i := 0; i < len(candies); i++ {
		if maxNumber < candies[i] {
			maxNumber = candies[i]
		}
	}
  
	for idx, val := range candies {
		if val+extraCandies >= maxNumber {
			result[idx] = true
		} else {
			result[idx] = false
		}
	}
	return result
}
