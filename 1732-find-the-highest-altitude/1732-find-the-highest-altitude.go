func largestAltitude(gain []int) int {
	result := make([]int, len(gain)+1)

	for i, v := range gain {
		result[i+1] = result[i] + v
	}

	max := 0
	for _, v := range result {
		if max < v {
			max = v
		}
	}
	return max
}
