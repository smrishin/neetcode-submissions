class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = float("inf")
        maxP = 0

        for p in prices:
            minBuy = min(p, minBuy)
            maxP = max(maxP, p - minBuy)
        
        return maxP
