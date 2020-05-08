class Solution:
    # originally went for a DFS implementation, but that is O(n^2)
    # as there could be n-1+n-2+n-3+...+1 edges => O(n+n^2) ~= O(n^2)
 
    # feels like a greedy problem up front, just need to spend
    # more time thinking about it.
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0
        for i, n in enumerate(nums):
            if i > max_jump:
                return False
            
            max_jump = max(max_jump, i + n)
            
        return True

