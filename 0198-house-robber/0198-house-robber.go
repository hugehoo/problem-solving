func rob(nums []int) int {

	if len(nums) < 2 {
		return nums[0]
	}

	dp := make([]int, len(nums))
	dp[0] = nums[0]
	if nums[1] > nums[0] {
		dp[1] = nums[1]
	} else {
		dp[1] = nums[0]
	}

	for i := 2 ; i< len(nums) ; i++ {
		if dp[i - 1] > nums[i] + dp[i  - 2] {
			dp[i] = dp[i - 1]
		} else {
			dp[i] = nums[i] + dp[i-2]
		}
	}
	return dp[len(nums) - 1]
}
