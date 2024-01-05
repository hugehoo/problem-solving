func canPlaceFlowers(flowerbed []int, n int) bool {
	count := 0
	for i := 0; i < len(flowerbed); i++ {
		if flowerbed[i] == 0 {
			emptyLeftPlot := i == 0 || flowerbed[i-1] == 0
			emptyRightPlot := i == len(flowerbed)-1 || (i < len(flowerbed)-1 && flowerbed[i+1] == 0)
			if emptyLeftPlot && emptyRightPlot {
				flowerbed[i] = 1
				count++
			}
		}
	}
	if count >= n {
		return true
	}
	return false
}
