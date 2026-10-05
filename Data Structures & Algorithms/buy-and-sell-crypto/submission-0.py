class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        best = 0
        r = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            elif prices[r] > prices[l]:
                best = max(prices[r] - prices[l], best)
            r += 1
            
        return best