func numberOfPairs(nums1 []int, nums2 []int, k int) int {
	result := 0
	for _, v := range nums1 {
		for _, w := range nums2 {
			m := v % (w * k)
			if m == 0 {
				result += 1
			}
		}

	}
	return result
}
