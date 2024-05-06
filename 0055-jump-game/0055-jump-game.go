func canJump(nums []int) bool {
    reachable := 0
	for i := 0; i < len(nums); i++ {
		if reachable >= len(nums)-1 {
			return true
		}
		if i > reachable {
			return false
		}
		reachable = max(reachable, nums[i]+i)
	}
	return true
}