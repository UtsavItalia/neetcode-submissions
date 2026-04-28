class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestDay = prices[0]
        maxProfit = 0

        for num in prices:
            if num < bestDay:
                bestDay = num
            maxProfit = max(maxProfit, num - bestDay)

        return maxProfit