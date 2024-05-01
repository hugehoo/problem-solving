func maxProfit(prices []int) int {
	var minPrice = prices[0]
	var maxProfit = 0
	for i := 1 ; i < len(prices) ; i++ {
		if prices[i] < minPrice {
			minPrice = prices[i]
		} else if prices[i] - minPrice > maxProfit {
			maxProfit = prices[i] - minPrice
		}
	}
	return maxProfit
}
