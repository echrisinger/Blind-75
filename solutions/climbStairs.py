class Solution:
    def climbStairs(self, n: int) -> int:
        if n in range(0, 3):
            return max(n, 1)
        
        prev1 = 2
        prev2 = 1
        for i in range(3, n+1):
            curr = prev1+prev2
            prev2 = prev1
            prev1 = curr
            
        return prev1
            
# O(n), O(1) space
