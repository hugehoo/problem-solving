func moveZeroes(nums []int)  {
    l := 0
    for idx := range nums{
        if nums[idx] != 0 {
            nums[l] = nums[idx]
            l++
        }
    }
    for ; l < len(nums) ; l++{
        nums[l] = 0
    }
    return
}