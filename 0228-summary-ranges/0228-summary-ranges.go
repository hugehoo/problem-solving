func summaryRanges(nums []int) []string {
	counter := 0
	var list []string

	for i, num := range nums {
		nextNum := num + 2
		if i != len(nums)-1 {
			nextNum = nums[i+1]
		}

		if nextNum-num <= 1 {
			counter++
			continue
		}

		startNum := num - counter
		if counter == 0 {
			list = append(list, fmt.Sprintf("%d", num))
		} else {
			list = append(list, fmt.Sprintf("%d->%d", startNum, num))
			counter = 0
		}

	}
	return list
}