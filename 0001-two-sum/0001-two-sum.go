func twoSum(nums []int, target int) []int {
    var ans []int
    numToIdx := make(map[int]int)
    
    for idx, num := range nums{
        expected := target - num
        
        if expectedIdx, exists := numToIdx[expected]; exists && expectedIdx != idx {
            ans = append(ans, idx, expectedIdx)
            break
        }
        
        numToIdx[num] = idx
    }
    
    return ans
}