# O(1) space, O(n) time
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub_array = nums[0]
        left = 0
        for n in nums:
            max_sub_array = max(max_sub_array, left + n)
            left = max(left + n, 0)
            
        return max_sub_array
        
