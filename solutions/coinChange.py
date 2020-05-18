class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        table = [-1]*(amount+1)
        table[0] = 0
        
        for curr_amt in range(1, amount+1):            
            subtotal_no = float('inf')
            for c in coins:
                coin_subtotal = curr_amt - c
                if coin_subtotal < 0:
                    break
                if table[coin_subtotal] >= 0:
                    subtotal_no = min(subtotal_no, table[coin_subtotal])
            
            if subtotal_no != float('inf'):
                table[curr_amt] = subtotal_no + 1
        
        return table[amount]
            
