class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lowestPrice = prices[0]

        for price in prices:
            if price < lowestPrice:
                lowestPrice = price
            maxProfit = max(maxProfit, price - lowestPrice)
            
        return maxProfit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lowestPrice = prices[0]

        for price in prices:
            if price < lowestPrice:
                lowestPrice = price
            maxProfit = max(maxProfit, price - lowestPrice)
            
        return maxProfit
