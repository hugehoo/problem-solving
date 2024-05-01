class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        return max_profit
        
# 오름차순인 부분 수열을 찾아서 
# 피봇 -> 나머지 절반에서 가장 큰 값을 찾고 차감
# 나머지 절반을 어케 찾을거임?
