class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr_min = float('inf')
        for p in prices:
            curr_min = min(curr_min, p)
            max_profit = max(p - curr_min, max_profit)
            
        return max_profit

