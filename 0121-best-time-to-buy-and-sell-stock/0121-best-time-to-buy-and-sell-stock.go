func maxProfit(prices []int) int {
	minPrice := prices[0]
	maxProfit := 0
	for _, price := range prices {
		maxProfit = int(math.Max(float64(price-minPrice), float64(maxProfit)))
		minPrice = int(math.Min(float64(minPrice), float64(price)))
	}
	return maxProfit
}