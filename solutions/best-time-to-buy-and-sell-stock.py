# O(n) time, O(1) space

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        max_profit = 0
        for i in range(1,len(prices)):
            curr_profit = prices[i] - buy_price
            max_profit = max(curr_profit, max_profit)
            buy_price = min(prices[i], buy_price)
            
        return max_profit
        
