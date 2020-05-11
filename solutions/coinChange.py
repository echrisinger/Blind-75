class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coin_counts = [0] * (amount+1)
            
        for curr_amt in range(1, amount+1):
            sub_val = float('inf')
            
            for c in coins:
                sub_amount = curr_amt - c
                if sub_amount >= 0:
                    sub_val = min(sub_val, coin_counts[sub_amount])
                        
                coin_counts[curr_amt] = sub_val + 1
        
        return coin_counts[amount] if coin_counts[amount] != float('inf') else -1
