func singleNumber(nums []int) int {
    
    dict := make(map[int] int)
    
    for _, num := range nums{
        dict[num] += 1
    }
    
    for num, count := range dict {
        if count == 1 {
            return num
        }
    }
    return -1


}